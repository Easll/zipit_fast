from os.path import isfile
import asyncio
import re
import pyzipper 
from telegram import Message, MessageEntity
import mimetypes
from datetime import datetime
import os
import uuid

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


def give_pagenation_info (page: int, page_size: int, content):

    floor = page*page_size

    if (len(content) - floor) > page_size:
        cieling = floor + page_size
        next_page = page + 1
    else:
        cieling = len(content)
        next_page = None
    
    if page > 0:
        pre_page = page - 1
    else:
        pre_page = None

    return (floor, cieling, pre_page, next_page)


async def _add_text_to_file (text, dir_path):
    file_path = os.path.join(dir_path, f"{uuid.uuid4().hex}.txt")

    with open(file_path, 'w', encoding= 'utf-8') as f:
        f.write(text)

    return file_path


# Matches both common ways a Telegram proxy link is written:
#   t.me/proxy?vpn=1&protocol=... or https://t.me/proxy?...
#   tg://proxy?... / tg://socks?... / tg://tcp?...
# Deliberately matches the *start* of a URL so we can anchor a full-URL
# extraction, and it also matches a bare label like "t.me/proxy".
PROXY_PATTERN = re.compile(r'(?:https?://)?t\.me/proxy|tg://(?:proxy|socks|tcp)', re.IGNORECASE)

# Any character that terminates a URL in plain text. Telegram wraps URLs in
# entities, so in the no-entity case (bare paste) the URL ends at whitespace.
_URL_END = re.compile(r'[\s\u2028\u2029]')


def _extract_full_url(text: str, match) -> str:
    """Expand a PROXY_PATTERN match to the end of its URL (keeps query params)."""
    end = _URL_END.search(text, match.end())
    # end.start() if matched else len(text) -- the upper bound of the slice.
    stop = end.start() if end else len(text)
    return text[match.start():stop]


def _iter_proxy_urls(text: str):
    """Yield every proxy URL in `text` (full URL, query params included).

    Advances past the *full* matched URL on each step so the tail of one URL
    (e.g. its query string) is never re-scanned as the start of a later one.
    """
    pos = 0
    while True:
        m = PROXY_PATTERN.search(text, pos)
        if not m:
            break
        url = _extract_full_url(text, m)
        yield url
        pos = m.start() + len(url)


def find_proxy_urls(text: str | None, entities) -> list[str]:
    """Return every *distinct* proxy URL carried by a message, in order.

    Telegram does not put the real href of a hyperlink into ``message.text``.
    A message like ``[label](https://t.me/proxy?a=1)`` has ``message.text ==
    "label"`` and the URL hidden in a ``MessageEntity.TEXT_LINK``. So we scan
    both the raw text and every link-style entity (their ``url`` attribute and
    the spanned substring). Duplicates (e.g. a URL that is both visible text
    and a linked entity over that same text) are collapsed into one entry.
    """
    found: list[str] = []
    seen: set[str] = set()

    def _record(url: str) -> None:
        if url and url not in seen:
            seen.add(url)
            found.append(url)

    # 1) The plain text itself may contain the URL(s).
    if text:
        for url in _iter_proxy_urls(text):
            _record(url)

    # 2) Hyperlink entities carry the real destination URL in their .url,
    #    which is invisible in message.text. Also handle cases where the
    #    entity's spanned text itself is a proxy.
    if entities:
        for ent in entities:
            if ent.type not in (MessageEntity.TEXT_LINK, MessageEntity.URL):
                continue
            candidates = []
            if ent.url:
                candidates.append(ent.url)
            if text:
                candidates.append(text[ent.offset:ent.offset + ent.length])
            for candidate in candidates:
                if not candidate:
                    continue
                for url in _iter_proxy_urls(candidate):
                    _record(url)

    return found


def find_proxy_url(text: str | None, entities) -> str | None:
    """Return the first proxy URL carried by a message, if any (back-compat)."""
    urls = find_proxy_urls(text, entities)
    return urls[0] if urls else None









