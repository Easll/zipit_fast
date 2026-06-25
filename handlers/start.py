from telegram import Update
from telegram.ext import ContextTypes
from massages import get_message
import keyboard

async def start (update : Update, context : ContextTypes.DEFAULT_TYPE):
    db = context.bot_data["db"]
    user_id = update.effective_user.id

    await db.ensure_user_exists (user_id)

    lang = await db.get_language (user_id)
    context.user_data['lang'] = lang

    await update.message.reply_text(get_message(lang, 'Welcome'), reply_markup=keyboard.get_greet_buttons())


async def help (update: Update, context):
    lang = context.user_data['lang']
    await update.message.reply_text(get_message(lang, 'Help'))

async def inline_start (update: Update, context):
    quary = update.callback_query
    await quary.answer()

    lang = context.user_data['lang']

    if quary.data == 'start_help':
        await quary.edit_message_text(get_message(lang, 'Help'))
    elif quary.data == 'start_language':
        await quary.edit_message_text(get_message(lang, 'Show_lang'), reply_markup=keyboard.get_lang_buttons())
    elif quary.data == 'start_fas':
        context.user_data['lang'] = 'fas'
        lang = context.user_data['lang']
        await quary.edit_message_text(get_message(lang, 'Chose_fas'))
    elif quary.data == 'start_eng':
        context.user_data['lang'] = 'en'
        lang = context.user_data['lang']
        await quary.edit_message_text(get_message(lang, 'Chose_eng'))
        


async def show_lang (update: Update, context):
    lang = context.user_data['lang']
    await update.message.reply_text(get_message(lang, 'Show_lang'), reply_markup=keyboard.get_lang_buttons())
