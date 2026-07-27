import asyncio
from logging import exception
from uuid import uuid4
import shutil
from aiosqlite import context
from pyzipper.zipfile import shutil
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from massages import get_message
import keyboard
import massages
from utils import identify_files, bytes_to_kb, build_archive, check_file_size, check_total_size
from massages import get_message
import os
import utils

ASKING_FOR_ARCHIVE_NAME = 1
ASKING_FOR_ENCRYPTION = 2
ASKING_FOR_PASSWORD = 3


async def add_files (update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = context.bot_data['db']
    lang = context.user_data.get ('lang', await db.get_language(update.effective_user.id))

    bot_message = await update.message.reply_text(get_message(lang=lang, key= 'Extracting_metadata'))

    metadata = identify_files(update.message)
    
    if check_file_size(file_size=metadata['size']):
        await db.add_pending_file(
                user_id = update.effective_user.id, 
                name = metadata['name'],
                file_id = metadata['file_id'],
                unique_id = metadata['unique_id'],
                size = metadata['size']
                ) 
    
        await bot_message.edit_text(get_message(lang=lang, key= 'Metadata_added').format(name = metadata['name'], size = str(bytes_to_kb(metadata['size']))))
    else:
        await update.message.reply_text(get_message(lang=lang, key='File_too_big'))


async def _get_files_logic (user_id, reply_func, context: ContextTypes.DEFAULT_TYPE):
    
    db = context.bot_data['db']
    lang = context.user_data.get ('lang', await db.get_language(user_id))
    
    data_dictionary = await db.get_pending_files(user_id = user_id)
    
    message_text = f"{get_message(lang=lang, key = 'Show_pending_files_I')} \n ===================== \n"
    count = 0
    for row in data_dictionary:
        count = count + 1
        message_text = message_text +f'({count}) \n'+ get_message(lang = lang, key = 'Show_pending_files_II').format(name = row['file_name'], size = bytes_to_kb(row['file_size'])) + '\n ===================== \n'

    await reply_func(message_text, reply_markup = keyboard.get_pending_files_buttons(lang= lang))


async def get_files (update : Update, context: ContextTypes.DEFAULT_TYPE):
    await _get_files_logic(user_id= update.effective_user.id, reply_func= update.message.reply_text, context= context)



async def _show_remove_buttons_logic (user_id, reply_func, context : ContextTypes.DEFAULT_TYPE):
    db = context.bot_data['db']
    lang = context.user_data.get ('lang', await db.get_language(user_id))
    
    files = await db.get_pending_files(user_id = user_id)
    
    if files:
        await reply_func(get_message(lang= lang, key= 'Remove_options'), reply_markup = keyboard.get_remove_buttons(files= files))

    else:
        await reply_func(get_message(lang = lang, key= 'No_remove_options'))



async def show_remove_buttons (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await _show_remove_buttons_logic (user_id= update.effective_user.id, reply_func= update.message.reply_text, context = context)



async def _ask_for_archive_name_logic (user_id, reply_func, context: ContextTypes.DEFAULT_TYPE):
    db = context.bot_data['db']
    lang = context.user_data.get ('lang', await db.get_language(user_id))
    
    pending_files = await db.get_pending_files(user_id = user_id)
    if pending_files:
        if check_total_size(files=pending_files):
            await reply_func(get_message(lang=lang, key='Ask_for_archive_name'), reply_markup = keyboard.get_cancel_button(lang= lang))
            return ASKING_FOR_ARCHIVE_NAME
        else:
            await reply_func(get_message(lang=lang, key='Archive_too_big'))
            return ConversationHandler.END
    else:
        await reply_func(get_message(lang= lang, key= 'No_pending_files'))
        return ConversationHandler.END

async def ask_for_archive_name (update: Update, context: ContextTypes.DEFAULT_TYPE):
    return (await _ask_for_archive_name_logic(user_id= update.effective_user.id, reply_func= update.message.reply_text, context= context))


async def recive_archive_name (update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = context.bot_data['db']
    lang = context.user_data.get ('lang', await db.get_language(update.effective_user.id))

    archive_name = update.message.text
    context.user_data['archive_name'] = archive_name

    await update.message.reply_text(get_message(lang=lang, key='Ask_for_encryption'), reply_markup= keyboard.get_ask_for_encryption_buttons(lang= lang))
    return ASKING_FOR_ENCRYPTION


async def _ask_for_password_logic (user_id, reply_func, context: ContextTypes.DEFAULT_TYPE):
    db = context.bot_data['db']
    lang = context.user_data.get ('lang', await db.get_language(user_id))

    await reply_func(get_message(lang=lang, key='Ask_for_password'), reply_markup = keyboard.get_cancel_button(lang= lang)) 
    return ASKING_FOR_PASSWORD

async def ask_for_password (update: Update, context: ContextTypes.DEFAULT_TYPE):
    return (await _ask_for_password_logic (user_id= update.effective_user.id, reply_func= update.message.reply_text, context= context))



COMPRESSION_SEMAPHORE = asyncio.Semaphore(2)

async def _build_send_archive_logic (user_id, reply_func_text, reply_func_doc, password, context: ContextTypes.DEFAULT_TYPE):
    db = context.bot_data['db']
    lang = context.user_data.get ('lang', await db.get_language(user_id))

    bot_message = await reply_func_text(get_message(lang=lang, key='Starting_compression'))
    
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tmp_dir_files = os.path.join(project_root, 'tmp_files', f"to_be_compressed_{user_id}_{uuid4().hex}")
    arhcive_path = os.path.join(project_root,'tmp_files', f"{user_id}_{uuid4().hex}.zip")

    pending_files = await db.get_pending_files(user_id = user_id)
    download_paths = []

    async with COMPRESSION_SEMAPHORE:
       try:
           os.makedirs(tmp_dir_files, exist_ok=True)
           seen_names = {}
           for file in pending_files:
               tg_file = await context.bot.get_file(file['file_id']) 
               local_path = os.path.join(tmp_dir_files, file['file_name'])

               if local_path in download_paths:
                   seen_names[local_path] += 1
                   name, ext = os.path.splitext(file['file_name'])
                   local_path = os.path.join(tmp_dir_files, f"{name}({seen_names[local_path]}){ext}")
               else:
                   seen_names[local_path] = 0

               await tg_file.download_to_drive(custom_path=local_path)
               download_paths.append(local_path)

           bot_message = await bot_message.edit_text(get_message(lang=lang, key='Compressing'))
           await build_archive(file_paths=download_paths, archive_save_path=arhcive_path, password=password)

           await bot_message.edit_text(get_message(lang=lang, key='Uploading'))
           with open (arhcive_path, 'rb') as f:
               await reply_func_doc(document=f, filename=f"{context.user_data['archive_name']}.zip")

           await db.mark_files_archived(user_id = user_id)

       except Exception as e:
           print (f'compression failed: {e}')
           await reply_func_text(get_message(lang = lang, key = 'Compression_failed'))

       finally:
           if os.path.exists(tmp_dir_files): shutil.rmtree(tmp_dir_files, ignore_errors=True)
           if os.path.exists(arhcive_path): os.remove(arhcive_path)
    context.user_data.clear()
    return ConversationHandler.END




async def build_archive_encrypted (update: Update, context: ContextTypes.DEFAULT_TYPE):
    password = update.message.text
    context.user_data['password'] = password

    return (await _build_send_archive_logic(user_id= update.effective_user.id, reply_func_text= update.message.reply_text, reply_func_doc= update.message.reply_document,password = password, context = context))



async def build_archive_un_encrypted (update: Update, context: ContextTypes.DEFAULT_TYPE):
    return (await _build_send_archive_logic(user_id= update.effective_user.id, reply_func_text= update.message.reply_text, reply_func_doc= update.message.reply_document,password = None, context = context))


async def _cancel_compression_logic (user_id, reply_func, context: ContextTypes.DEFAULT_TYPE):
    db = context.bot_data['db']
    lang = context.user_data.get ('lang', await db.get_language(user_id))

    await reply_func(get_message(lang= lang, key='Compression_canceled'))
    context.user_data.clear()
    return ConversationHandler.END


async def cancel_compression (update: Update, context: ContextTypes.DEFAULT_TYPE):
    return (await _cancel_compression_logic(user_id= update.effective_user.id, reply_func= update.message.reply_text, context = context))
                

                
async def inline_show_files (update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = context.bot_data['db']
    lang = context.user_data.get ('lang', await db.get_language(update.effective_user.id))
    
    query = update.callback_query
    await query.answer()

    if query.data == 'zipnoconv_show_files':
        await _get_files_logic(user_id= update.effective_user.id, reply_func= query.message.reply_text, context = context)



async def inline_start_compression (update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = context.bot_data['db']
    lang = context.user_data.get ('lang', await db.get_language(update.effective_user.id))
     
    query = update.callback_query
    await query.answer()

    if query.data == 'zipstartconv':
        return (await _ask_for_archive_name_logic(user_id= update.effective_user.id, reply_func= query.message.reply_text, context = context))



async def inline_cancel_compression (update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = context.bot_data['db']
    lang = context.user_data.get ('lang', await db.get_language(update.effective_user.id))
     
    query = update.callback_query
    await query.answer()

    if query.data == 'zipcancelconv_cancel_compression':
        return (await _cancel_compression_logic (user_id= update.effective_user.id, reply_func= query.message.reply_text, context = context))




async def inline_compression_flow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = context.bot_data['db']
    lang = context.user_data.get ('lang', await db.get_language(update.effective_user.id))
     
    query = update.callback_query
    await query.answer()

    if query.data == 'zipconv_encrypt':
        return (await _ask_for_password_logic(user_id= update.effective_user.id, reply_func= query.message.reply_text, context = context))

    elif query.data == 'zipconv_dont_encrypt':
        return (await _build_send_archive_logic (user_id= update.effective_user.id, reply_func_text= query.message.reply_text, reply_func_doc= query.message.reply_document ,password = None, context = context))






