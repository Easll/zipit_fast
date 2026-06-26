import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from handlers.start import start, help, show_lang, inline_start
import asyncio
from database import Database

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
DB_PATH = os.getenv("ZIP_IT_FAST_DB_PATH")

async def init_db (app : Application):
    db = Database(DB_PATH)
    await db.init()
    app.bot_data['db'] = db

async def close_db (app : Application):
    db = app.bot_data.get('db')
    if db:
        await db.close()
        print ('Database connection closed')


def main():
    app = Application.builder().token(TOKEN).post_init(init_db).post_shutdown(close_db).build()
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('language', show_lang))

    app.add_handler(CallbackQueryHandler(inline_start, pattern='^start_'))


    app.run_polling()


if __name__ == "__main__":
    main()
