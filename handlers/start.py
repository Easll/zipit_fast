from telegram import Update
import massages
import keyboard

async def start (update : Update, context):
    await update.message.reply_text(massages.WELCOME, reply_markup=keyboard.get_greet_buttons())


async def help (update: Update, context):
    await update.message.reply_text(massages.HELP)

async def inline_start (update: Update, context):
    quarry = update.callback_query
    await quarry.answer()

    if quarry.data == 'start_help':
        await quarry.edit_message_text(massages.HELP)
    elif quarry.data == 'start_language':
        await quarry.edit_message_text(massages.SHOW_LANG, reply_markup=keyboard.get_lang_buttons())
    elif quarry.data == 'start_fas':
        await quarry.edit_message_text(massages.CHOSE_FAS)
    elif quarry.data == 'start_eng':
        await quarry.edit_message_text(massages.CHOSE_ENG)
        


async def show_lang (update: Update, context):
    await update.message.reply_text(massages.SHOW_LANG, reply_markup=keyboard.get_lang_buttons())