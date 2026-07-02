import pyzipper as zp
from telegram import Message
import mimetypes
from datetime import datetime

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

#def zip_it ()

#def zip_them ()    
