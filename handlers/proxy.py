import asyncio
import os
import uuid
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from massages import get_message
import keyboard
import utils
from utils import find_proxy_urls
import secrets
import string
import random
import shutil
from telegram.constants import ParseMode


TEXT_TO_FILE_SEMAPHORE = asyncio.Semaphore(2)

async def _compress_proxy_logic  (user_id, reply_func, reply_func_doc, lang, text, context: ContextTypes.DEFAULT_TYPE):
    bot_message = await reply_func(get_message(lang = lang, key= 'Proxy_recognized'))

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tmp_dir_files = os.path.join(project_root, 'tmp_files', f"proxy_text_{user_id}_{uuid.uuid4().hex}")
    archive_path = os.path.join(project_root, 'tmp_files', f"{user_id}_{uuid.uuid4().hex}.zip")
    password = ''.join(secrets.choice(string.hexdigits) for _ in range (6))

    async with TEXT_TO_FILE_SEMAPHORE:
        try:
            os.makedirs(tmp_dir_files, exist_ok=True)
            file_path = await utils._add_text_to_file(text=text, dir_path=tmp_dir_files)

            await utils.build_archive(file_paths=[file_path], archive_save_path= archive_path, password=password)

            bot_message = await bot_message.edit_text(get_message(lang=lang, key= 'Uploading'))
            
            archive_name = ''.join(random.choices(string.ascii_uppercase, k=6))
            with open (archive_path, 'rb') as f:
                await reply_func_doc(document = f, filename = f"{archive_name}.zip")

            password_message = get_message(lang=lang, key='Proxy_password').format(password = password)    
            await reply_func(password_message, parse_mode=ParseMode.HTML)

        except Exception as e:
            print (f"proxy compresstion failed: {e}")
            await reply_func (get_message(lang=lang, key='Proxy_compression_failed'))

        finally:
            if os.path.exists(tmp_dir_files): shutil.rmtree(tmp_dir_files, ignore_errors= True)
            if os.path.exists(archive_path): os.remove(archive_path)
            

async def compress_proxy (update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = context.bot_data['db']
    lang = context.user_data.get ('lang', await db.get_language(update.effective_user.id))

    proxy_urls = find_proxy_urls(update.message.text, update.message.entities)

    await _compress_proxy_logic (
            user_id= update.effective_user.id,
            reply_func= update.message.reply_text,
            reply_func_doc= update.message.reply_document,
            lang= lang,
            text= "\n".join(proxy_urls) if proxy_urls else update.message.text,
            context= context,)





