import os
from dotenv import load_dotenv
from telegram.ext import Application

load_dotenv()
TOKEN = os.get_env("BOT_TOKEN")

def main():
    app = Application.builder().token(TOKEN).build()

    app.run_polling()


if __name__ == "__main__":
    main()