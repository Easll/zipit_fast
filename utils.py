from os.path import isfile
import asyncio
import pyzipper 
from telegram import Message
import mimetypes
from datetime import datetime
import os

def identify_files (message: Message):

    file_obj = None

    if message.document:
        file_obj = message.document
        if file_obj.file_name:
            file_obj_name = file_obj.file_name
        else:
            ext = mimetypes.guess_extension(file_obj.mime_type) if file_obj.mime_type else None
            default_ext = '.bin'
            file_obj_name = f"Un_Named_File_{file_obj.file_unique_id}{ext or default_ext}"
    
    elif message.video:
        file_obj = message.video
        if file_obj.file_name:
            file_obj_name = file_obj.file_name
        else:
            ext = mimetypes.guess_extension(file_obj.mime_type) if file_obj.mime_type else None
            default_ext = '.mp4'
            file_obj_name = f'Un_Named_Video_{file_obj.file_unique_id}{ext or default_ext}'
    
    elif message.audio:
        file_obj = message.audio
        if file_obj.file_name:
            file_obj_name = file_obj.file_name
        else:
            ext = mimetypes.guess_extension(file_obj.mime_type) if file_obj.mime_type else None
            default_ext = '.mp3'
            file_obj_name = f'Un_Named_Audio_{file_obj.file_unique_id}{ext or default_ext}'
    
    elif message.photo:
        file_obj = message.photo[-1]

        file_obj_name = f'Photo_{file_obj.file_unique_id}.jpg'
  
    elif message.animation:
        file_obj = message.animation
        if file_obj.file_name:
            file_obj_name = file_obj.file_name
        else:
            ext = mimetypes.guess_extension(file_obj.mime_type) if file_obj.mime_type else None
            default_ext = '.gif'
            file_obj_name = f'Un_Named_Gif_{file_obj.file_unique_id}{ext or default_ext}'
    
    elif message.voice:
        file_obj = message.voice
        file_obj_name = f"Voice_{file_obj.file_unique_id}.ogg"

    elif message.video_note:
        file_obj = message.video_note
        file_obj_name = f"Live_video_{file_obj.file_unique_id}.mp4"

    if not file_obj:
       return None

    output = {
            'name': file_obj_name,
            'unique_id': file_obj.file_unique_id,
            'file_id': file_obj.file_id,
            'size': file_obj.file_size,}
    
    return output


def bytes_to_kb (bt: int) -> str:
    kb = bt // 1024
    if kb < 1:
        return '>1 KB'
    return f"{kb} KB"


def _build_archive (file_paths: list [str], archive_save_path: str, password: str | None = None):
    encryption = pyzipper.WZ_AES if password else None
    seen_names = {}
    with pyzipper.AESZipFile(archive_save_path, 'w', compression = pyzipper.ZIP_DEFLATED, encryption = encryption, allowZip64 = False) as zp:
        
        if password:
            zp.setpassword(password.encode('utf-8'))

        for file_path in file_paths:
            if not os.path.isfile(file_path):
                print (f"file {file_path} wasn't found")
                continue

            basename = os.path.basename(file_path)
            name, ext = os.path.splitext(basename)

            if basename in seen_names:
                seen_names[basename] += 1
                arcname = f"{name}({seen_names[basename]}){ext}"
            else:
                seen_names[basename] = 0
                arcname = basename

            zp.write(file_path, arcname=arcname)


async def build_archive  (file_paths: list [str], archive_save_path: str, password: str | None = None):
    await asyncio.to_thread(_build_archive, file_paths, archive_save_path, password)
 
 
def check_file_size (file_size : int):
    if file_size > 20900000:
        return False
    return True


def check_total_size (files : dict):
    total_size = 0
    for file in files:
        total_size += file['file_size']
    if total_size > 52400000:
        return False
    return True











