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
                language TEXT DEFAULT 'en');"""

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

        
    async def close(self):
        await self.conn.close()
