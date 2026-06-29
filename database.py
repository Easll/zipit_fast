import aiosqlite
import asyncio

class Database:

    def __init__(self, db_path : str):
        self.db_path = db_path
        self._lock = asyncio.Lock()
    
    async def init (self):
        self.conn = await aiosqlite.connect(self.db_path)
        self.conn.row_factory = aiosqlite.Row
        await self._create_tables ()

    async def _create_tables (self):
        async with self._lock:
            await self.conn.executescript("""
                CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                language TEXT DEFAULT 'en');
                            
                CREATE TABLE IF NOT EXISTS compression_files (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    file_id TEXT NOT NULL,
                    file_unique_id TEXT NOT NULL,
                    file_name TEXT NOT NULL,
                    file_size INTEGER NOT NULL,
                    status TEXT NOT NULL DEFAULT 'pending',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                );
            
                -- Index for fast lookups when querying pending files by user
                CREATE INDEX IF NOT EXISTS idx_compression_files_user_status 
                ON compression_files(user_id, status);
            
                -- Index for fast lookups by created_at (for ordering)
                CREATE INDEX IF NOT EXISTS idx_compression_files_created_at 
                ON compression_files(created_at);
                """

            )
            await self.conn.commit()

    async def ensure_user_exists (self, user_id, default_language = 'en'):
        async with self._lock:
            await self.conn.execute(
                    " INSERT OR IGNORE INTO users (user_id, language) VALUES (?, ?)",
                    (user_id, default_language),
                    )
            await self.conn.commit()
    
    async def get_language(self, user_id):
        async with self._lock:
            cursor = await self.conn.execute(
                "SELECT language FROM users WHERE user_id = ? ",
                (user_id,)
            )
            
            row = await cursor.fetchone()
            return row['language'] if row else 'en'
        
    async def set_language (self, user_id, lang):
        async with self._lock:
            await self.conn.execute(
            "INSERT INTO users (user_id, language) VALUES (?, ?) "
            "ON CONFLICT(user_id) DO UPDATE SET language = ?",
            (user_id, lang, lang),
        )
        
        await self.conn.commit()
    
    async def add_pending_file (self, user_id, name, file_id, unique_id, size):
        async with self._lock:
            await self.conn.execute(
            """INSERT INTO compression_files 
                (user_id, file_id, file_unique_id, file_name, file_size, status) 
                VALUES (?, ?, ?, ?, ?, 'pending')""",
                (user_id, file_id, unique_id, name, size)
                )
            await self.conn.commit()
        
    async def get_pending_files (self, user_id):
        async with self._lock:
            cursor = await self.conn.execute(
            """SELECT id, file_id, file_unique_id, file_name, file_size, created_at 
               FROM compression_files 
               WHERE user_id = ? AND status = 'pending' 
               ORDER BY created_at ASC""",
            (user_id,)
            )
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]

    async def mark_files_archived (self, user_id):
        async with self._lock:
            self.conn.execute(
            """UPDATE compression_files 
               SET status = 'archived' 
               WHERE user_id = ? AND status = 'pending'""",
               (user_id,))
            await self.conn.commit()


    async def close(self):
        await self.conn.close()
