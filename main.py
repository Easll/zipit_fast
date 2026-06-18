import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from handlers.start import start, help, show_lang, inline_start
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('language', show_lang))

    app.add_handler(CallbackQueryHandler(inline_start, pattern='^start_'))

    app.run_polling()


if __name__ == "__main__":
    main()