import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, filters
from handlers.start import start, help, show_lang, inline_start
from handlers.zip import ASKING_FOR_ARCHIVE_NAME, ASKING_FOR_ENCRYPTION, ASKING_FOR_PASSWORD, ask_for_password, get_files, add_files, ask_for_archive_name, ask_for_password, recive_archive_name, build_archive_encrypted, build_archive_un_encrypted, cancel_compression, inline_show_files
import asyncio
from database import Database

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
DB_PATH = os.getenv("ZIP_IT_FAST_DB_PATH")
TMP_PATH = os.getenv("ZIP_IT_FAST_TMP_PATH")

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
    app.add_handler(CallbackQueryHandler(inline_show_files, pattern= '^zipnoconv_'))

    app.add_handler(CommandHandler('show_files', get_files))

    app.add_handler(ConversationHandler(
        entry_points=[CommandHandler('compress', ask_for_archive_name)],
        states={
            ASKING_FOR_ARCHIVE_NAME:[MessageHandler(filters.TEXT & ~filters.COMMAND, recive_archive_name)],
            ASKING_FOR_ENCRYPTION:[
                CommandHandler('encrypt', ask_for_password),
                CommandHandler('dont_encrypt', build_archive_un_encrypted)
                ],
            ASKING_FOR_PASSWORD:[MessageHandler(filters.TEXT & ~filters.COMMAND, build_archive_encrypted)]
            },
        fallbacks=[CommandHandler('cancel', cancel_compression)]
        )) 

    app.add_handler(MessageHandler(filters.ATTACHMENT, add_files))


    app.run_polling()


if __name__ == "__main__":
    main()
