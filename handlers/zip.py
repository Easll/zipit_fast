from telegram import Update
from telegram.ext import ContextTypes
from massages import get_message
import keyboard
import massages
from utils import identify_files
from massages import get_message

async def add_files (update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = context.bot_data['db']
    lang = context.user_data.get ('db', await db.get_language(update.effective_user.id))

    await update.message.reply_text(get_message(lang=lang, key= 'Extracting_metadata'))

    metadata = await identify_files(update.message)

    await db.add_pending_file(
            user_id = update.effective_user.id, 
            name = metadata['name'],
            file_id = metadata['file_id'],
            unique_id = metadata['unique_id'],
            size = metadata['size']
            ) 
    
    await update.message.reply_text(get_message(lang=lang, key= 'Metadata_added').format(name = metadata['name'], size = str(metadata['size'])))


async def get_files (update:Update, context: ContextTypes.DEFAULT_TYPE):
    
    db = context.bot_data['db']
    lang = context.user_data.get ('db', await db.get_language(update.effective_user.id))
    
    data_dictionary = await db.get_pending_files(user_id = update.effective_user.id)
    
    message_text = ""
    for row in data_dictionary:
        message_text = message_text + get_message(lang = lang, key = 'Show_pending_files').format(name = row['file_name'], size = row['file_size']) + '\n'
    await update.message.reply_text(message_text)





