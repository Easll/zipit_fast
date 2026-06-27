import pyzipper as zp
from telegram import Message
import mimetypes
from datetime import datetime

def identify_files (message: Message):
    if message.document:
        file_obj = message.document
        if file_obj.name:
            file_obj_name = file_obj.name
        else:
            ext = mimetypes.guess_extension(file_obj.mime_type) if file_obj.mime_type else None
            file_obj_name = f'Un_Named_File{file_obj.file_unique_id}{ext or '.bin'}'
    
    elif message.video:
        file_obj = message.video
        if file_obj.name:
            file_obj_name = file_obj.name
        else:
            ext = mimetypes.guess_extension(file_obj.mime_type) if file_obj.mime_type else None
            file_obj_name = f'Un_Named_Video{file_obj.file_unique_id}{ext or '.mp4'}'
    
    elif message.audio:
        file_obj = message.audio
        if file_obj.name:
            file_obj_name = file_obj.name
        else:
            ext = mimetypes.guess_extension(file_obj.mime_type) if file_obj.mime_type else None
            file_obj_name = f'Un_Named_Audio{file_obj.file_unique_id}{ext or '.mp3'}'
    
    elif message.photo:
        file_obj = message.photo[-1]

        ext = mimetypes.guess_extension(file_obj.mime_type) if file_obj.mime_type else None
        file_obj_name = f'Un_Named_Photo{file_obj.file_unique_id}{ext or '.jpg'}'


#def zip_it ()

#def zip_them ()    
