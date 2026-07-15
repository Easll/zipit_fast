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

    await update.message.reply_text(get_message(lang, 'Welcome'), reply_markup=keyboard.get_greet_buttons(lang = lang))


async def help (update: Update, context):
    db = context.bot_data['db']
    lang = context.user_data.get ('lang', await db.get_language(update.effective_user.id))
    await update.message.reply_text(get_message(lang, 'Help'))

async def inline_start (update: Update, context):
    quary = update.callback_query
    await quary.answer()

    db = context.bot_data['db']

    lang = context.user_data.get ('lang', await db.get_language(update.effective_user.id))

    if quary.data == 'start_help':
        await quary.edit_message_text(get_message(lang, 'Help'))
    elif quary.data == 'start_language':
        await quary.edit_message_text(get_message(lang, 'Show_lang'), reply_markup=keyboard.get_lang_buttons())

    elif quary.data == 'start_fas':

        await db.set_language(user_id = update.effective_user.id, lang = 'fas')
        context.user_data['lang'] = 'fas'
        lang = context.user_data['lang']
        await quary.edit_message_text(get_message(lang, 'Chose_fas'))

    elif quary.data == 'start_eng':

        await db.set_language(user_id = update.effective_user.id, lang = 'en')
        context.user_data['lang'] = 'en'
        lang = context.user_data['lang']
        await quary.edit_message_text(get_message(lang, 'Chose_en'))
        


async def show_lang (update: Update, context):
    db = context.bot_data['db']
    lang = context.user_data.get ('lang', await db.get_language(update.effective_user.id))
    await update.message.reply_text(get_message(lang, 'Show_lang'), reply_markup=keyboard.get_lang_buttons())
