from telegram import Update
from telegram.ext import ContextTypes
from massages import get_message
import keyboard
from utils import identify_files
from massages import get_message

def add_files (update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = context.bot_data['db']
    lang = context.user_data.get ('db', await db.get_language(update.effective_user.id))

    update.message.reply_text(get_message(lang=lang, key= 'Extracting_metadata'))

    metadata = identify_files(update.message)

    db.add_pending_file(
            user_id = update.effective_user.id, 
            name = metadata['name'],
            file_id = metadata['file_id'],
            unique_id = metadata['unique_id'],
            size = metadata['size']
            ) 
    update.message.reply_text(get_message(lang=lang, key= 'Metadata_added').format(name = metadata['name'], size = str(metadata['size'])))

