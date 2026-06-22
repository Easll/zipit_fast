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

    async def _create_tebles (self):
        async with self._lock:
            await self.conn.executescript("""
                CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                language TEXT DEFAULT 'en');"""

            )
            await self.conn.commit()
