from telegram.ext import CommandHandler
from telegram import Update
import massages
import keyboard

async def start (update : Update, context):
    await update.message.reply_text(massages.WELCOME, reply_markup=keyboard.get_greet_buttons())


async def help (update: Update, context):
    await update.message.reply_text(massages.HELP)