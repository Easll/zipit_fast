from telegram import Update
from telegram.ext import ContextTypes
from massages import get_message
import keyboard
import massages
from utils import identify_files, bytes_to_kb
from massages import get_message

async def add_files (update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = context.bot_data['db']
    lang = context.user_data.get ('db', await db.get_language(update.effective_user.id))

    await update.message.reply_text(get_message(lang=lang, key= 'Extracting_metadata'))

    metadata = identify_files(update.message)

    await db.add_pending_file(
            user_id = update.effective_user.id, 
            name = metadata['name'],
            file_id = metadata['file_id'],
            unique_id = metadata['unique_id'],
            size = metadata['size']
            ) 
    
    await update.message.reply_text(get_message(lang=lang, key= 'Metadata_added').format(name = metadata['name'], size = str(bytes_to_kb(metadata['size']))))


async def get_files (update:Update, context: ContextTypes.DEFAULT_TYPE):
    
    db = context.bot_data['db']
    lang = context.user_data.get ('db', await db.get_language(update.effective_user.id))
    
    data_dictionary = await db.get_pending_files(user_id = update.effective_user.id)
    
    message_text = f"{get_message(lang=lang, key = 'Show_pending_files_I')} \n ===================== \n"
    count = 0
    for row in data_dictionary:
        count = count + 1
        message_text = message_text +f'({count}) \n'+ get_message(lang = lang, key = 'Show_pending_files_II').format(name = row['file_name'], size = bytes_to_kb(row['file_size'])) + '\n ===================== \n'
    await update.message.reply_text(message_text)




