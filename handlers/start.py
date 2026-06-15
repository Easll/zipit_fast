from telegram.ext import CommandHandler
from telegram import Update
import massages

async def start (update : Update, context):
    await update.message.reply_text(massages.WELCOME)

