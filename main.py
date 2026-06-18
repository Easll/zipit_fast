import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler
from handlers.start import start
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start', start))

    app.run_polling()


if __name__ == "__main__":
    main()