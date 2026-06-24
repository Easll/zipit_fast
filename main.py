import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from handlers.start import start, help, show_lang, inline_start
import asyncio
from database import Database

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
DB_PATH = os.getenv("ZIP_IT_FAST_DB_PATH")

async def main():
    app = Application.builder().token(TOKEN).build()

    db = Database(DB_PATH)
    await db.init
    app.bot_data['db'] = db
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('language', show_lang))

    app.add_handler(CallbackQueryHandler(inline_start, pattern='^start_'))

    app.add_shutdown_callback(lambda app: db.close())

    await app.run_polling()


if __name__ == "__main__":
    asyncio.run(main())