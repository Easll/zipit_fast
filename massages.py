#English messages



EN_WELCOME = """
👋 Hi!

🤖 I'm Zipit_Fast!

📂 Send me your files and I'll compress them (with 🔒 encryption if you want) and send them back to you!            

🔴 /help for more info 
🅰 /language to change the language. (Currently supporting English and Persian)
"""
EN_HELP = """
placeholder text
"""

EN_SHOW_LANG = """
🅰 Choose your language:
"""

EN_CHOSE_ENG = """
✅ English was chosen.

You can always change the language from the main menu.
"""

EN_EXTRACTING_METADATA = """
⚙️ Extracting metadata..."""

EN_METADATA_ADDED = """
✅ Added to your pending files, ready to be archived:

📄 Name: {name}
⚖️ Size: {size}
"""

EN_SHOW_PENDING_FILES_I = """
📁 Your pending files:
"""

EN_SHOW_PENDING_FILES_II = """
📄 Name: {name}
⚖️ Size: {size}
"""

EN_ASKING_FOR_ARCHIVE_NAME = """
Please enter a name for your archive:
"""

EN_ASKING_FOR_ENCRYPTION = """
🔒 Do you want your archive to be encrypted?
"""

EN_ASKING_FOR_PASSWORD = """
🔑 Please enter a password for your archive:
"""

EN_STARTING_COMPRESSION = """
⬇️ Downloading files..."""

EN_COMPRESSING = """
🗜️ Compressing files..."""

EN_UPLOADING = """
⬆️ Uploading archive..."""

EN_COMPRESSION_FAILED = """
❌ Compression failed. Please try again.
"""

EN_COMPRESSION_CANCELED = """
⏹️ Operation canceled.
"""

EN_NO_PENDING_FILES = """
📭 You have no pending files.
"""

EN_FILE_TOO_BIG = """
⚠️ Error: The bot is currently in Test mode and cannot download files bigger than 20 MB.
"""

EN_ARCHIVE_TOO_BIG = """
⚠️ Error: The total size of your archive exceeds 50 MB. The bot is currently in test mode and cannot upload files bigger than 50 MB.
"""

EN_REMOVE_OPTIONS = """
🗑️ Which file do you want to remove from your pending files?
"""

EN_NO_REMOVE_OPTIONS = """
You have no pending files to remove.
"""

EN_FILE_REMOVED = """
✅ Removed successfully.

🗑️ Which file do you want to remove next?
"""

EN_FILE_REMOVED_NO_MORE = """
✅ Removed successfully.

You have no more pending files to remove.
"""

EN_PROXY_RECOGNIZED = """
Proxy recognized. Making an encrypted zip..."""

EN_PROXY_PASSWORD = """
Password: <code>{password}</code>"""


#Farsi messages
FAS_WELCOME = """
👋 سلام!

 من Zipit_Fast هستم!

📂 فایل‌هات رو برام بفرست تا فشرده‌شون کنم (با امکان 🔒 رمزگذاری) و برات بفرستم!            

🔴 برای راهنمایی /help 

🅰 برای تغییر زبان /language
"""

FAS_HELP = """
این بخش در حال طراحی است

"""

FAS_SHOW_LANG = """
🅰 زبان مورد نظر خود را انتخاب کنید:
"""

FAS_CHOSE_FAS = """
✅ زبان فارسی انتخاب شد.

همیشه می‌توانید زبان را از منوی اصلی تغییر دهید.
"""

FAS_EXTRACTING_METADATA = """
⚙️ در حال استخراج مشخصات...""" 

FAS_METADATA_ADDED = """
✅ به لیست فایل‌های شما اضافه شد و آماده فشرده‌سازی است:

📄 نام: {name}
⚖️ اندازه: {size}
"""

FAS_SHOW_PENDING_FILES_I = """
📁 فایل‌های در انتظار (آرشیو نشده) شما:
"""

FAS_SHOW_PENDING_FILES_II = """
📄 نام: {name}
⚖️ اندازه: {size}
"""

FAS_ASKING_FOR_ARCHIVE_NAME = """
لطفاً یک نام برای آرشیو خود انتخاب کنید:"""

FAS_ASKING_FOR_ENCRYPTION = """
🔒 آیا می‌خواهید آرشیو شما رمزگذاری شود؟
"""

FAS_ASKING_FOR_PASSWORD = """
🔑 لطفاً یک رمز عبور برای آرشیو خود وارد کنید:"""

FAS_STARTING_COMPRESSION = """
⬇️ در حال دانلود فایل‌ها..."""

FAS_COMPRESSING = """
🗜️ در حال فشرده‌سازی..."""

FAS_UPLOADING = """
⬆️ در حال آپلود آرشیو..."""

FAS_COMPRESSION_FAILED = """
❌ فشرده‌سازی با خطا مواجه شد. لطفاً دوباره تلاش کنید."""

FAS_COMPRESSION_CANCELED = """
⏹️ عملیات لغو شد."""

FAS_NO_PENDING_FILES = """
شما هیچ فایل در انتظاری ندارید.
"""

FAS_FILE_TOO_BIG = """
⚠️ خطا: بات در حال حاضر در مرحله تست قرار دارد و نمی‌تواند فایل‌های بزرگتر از 20 مگابایت را دانلود کند."""

FAS_ARCHIVE_TOO_BIG = """
⚠️ خطا: حجم آرشیو شما از 50 مگابایت فراتر رفته است. بات در حال حاضر در مرحله تست قرار دارد و نمی‌تواند آرشیوهای بزرگتر از 50 مگابایت را آپلود کند."""

FAS_REMOVE_OPTIONS = """
🗑️ کدام فایل را می‌خواهید از لیست فایل‌های در انتظار حذف کنید؟
"""

FAS_NO_REMOVE_OPTIONS = """
📭 فایلی برای حذف وجود ندارد.
"""

FAS_FILE_REMOVED = """
✅ فایل با موفقیت حذف شد.

🗑️ کدام فایل بعدی را می‌خواهید حذف کنید؟"""

FAS_FILE_REMOVED_NO_MORE = """
✅ فایل با موفقیت حذف شد.

📭 فایلی برای حذف باقی نمانده است."""


FAS_PROXY_RECOGNIZED = """
پروکسی تشخیص داده شد. در حال ساخت زیپ رمزگزاری شده ..."""

FAS_PROXY_PASSWORD = """
رمز: <code>{password}</code>"""

#The dictionary


MESSAGES = {
    'en': {
        'Welcome' : EN_WELCOME,
        'Help' : EN_HELP,
        'Show_lang' : EN_SHOW_LANG,
        'Chose_en' : EN_CHOSE_ENG,
        'Extracting_metadata': EN_EXTRACTING_METADATA,
        'Metadata_added': EN_METADATA_ADDED,
        'Show_pending_files_I': EN_SHOW_PENDING_FILES_I,
        'Show_pending_files_II': EN_SHOW_PENDING_FILES_II,
        'Ask_for_archive_name': EN_ASKING_FOR_ARCHIVE_NAME,
        'Ask_for_encryption': EN_ASKING_FOR_ENCRYPTION,
        'Ask_for_password': EN_ASKING_FOR_PASSWORD,
        'Starting_compression': EN_STARTING_COMPRESSION,
        'Compressing': EN_COMPRESSING,
        'Uploading': EN_UPLOADING,
        'Compression_failed': EN_COMPRESSION_FAILED,
        'Compression_canceled': EN_COMPRESSION_CANCELED,
        'No_pending_files': EN_NO_PENDING_FILES,
        'File_too_big': EN_FILE_TOO_BIG,
        'Archive_too_big': EN_ARCHIVE_TOO_BIG,
        'Remove_options': EN_REMOVE_OPTIONS,
        'File_removed': EN_FILE_REMOVED,
        'File_removed_no_more_files': EN_FILE_REMOVED_NO_MORE,
        'Proxy_recognized': EN_PROXY_RECOGNIZED,
        'Proxy_password': EN_PROXY_PASSWORD,
    },

    'fas': {
        'Welcome' : FAS_WELCOME,
        'Help' : FAS_HELP,
        'Show_lang' : FAS_SHOW_LANG,
        'Chose_fas' : FAS_CHOSE_FAS,
        'Extracting_metadata' : FAS_EXTRACTING_METADATA,
        'Metadata_added' : FAS_METADATA_ADDED,
        'Show_pending_files_I': FAS_SHOW_PENDING_FILES_I,
        'Show_pending_files_II': FAS_SHOW_PENDING_FILES_II,
        'Ask_for_archive_name': FAS_ASKING_FOR_ARCHIVE_NAME,
        'Ask_for_encryption': FAS_ASKING_FOR_ENCRYPTION,
        'Ask_for_password': FAS_ASKING_FOR_PASSWORD,
        'Starting_compression': FAS_STARTING_COMPRESSION,
        'Compressing': FAS_COMPRESSING,
        'Uploading': FAS_UPLOADING,
        'Compression_failed': FAS_COMPRESSION_FAILED,
        'Compression_canceled': FAS_COMPRESSION_CANCELED,
        'No_pending_files': FAS_NO_PENDING_FILES,
        'File_too_big': FAS_FILE_TOO_BIG,
        'Archive_too_big': FAS_ARCHIVE_TOO_BIG,
        'Remove_options': FAS_REMOVE_OPTIONS,
        'File_removed': FAS_FILE_REMOVED,
        'File_removed_no_more_files': FAS_FILE_REMOVED_NO_MORE,
        'Proxy_recognized': FAS_PROXY_RECOGNIZED,
        'Proxy_password': FAS_PROXY_PASSWORD,
    }
}


# The dict function

def get_message (lang : str, key: str):
    lang_dict = MESSAGES.get(lang, 'en')

    return lang_dict.get(key, key)

#Button Names

#English

BT_EN_LANGUAGE = '🅰 Language'

BT_EN_HELP = '🔴 Help'

BT_EN_SHOW_FILES = '📁 Pending Files'

BT_EN_COMPRESS = '🗜️ Compress'

BT_EN_CANCEL_COMPRESSION = '❌ Cancel'

BT_EN_ENCRYPT = '🔒 Encrypted'

BT_EN_DONT_ENCRYPT = '🔓 Unencrypted'

BT_EN_REMOVE_FILES = '🗑️ Remove Files'

BT_EN_NEXT = '➡️ Next'

BT_EN_BACK = '⬅️ Back'

#Farsi

BT_FAS_LANGUAGE = 'زبان'

BT_FAS_HELP = 'راهنمایی'

BT_FAS_SHOW_FILES = '📁 فایل های در انتظار'

BT_FAS_COMPRESS = '🗜️ فشرده سازی'

BT_FAS_CANCEL_COMPRESSION = '❌ لغو'

BT_FAS_ENCRYPT = '🔒 با رمزنگاری'

BT_FAS_DONT_ENCRYPT = '🔓 بدون رمزنگاری'

BT_FAS_REMOVE_FILES = '🗑️ حذف فایل ها'

BT_FAS_NEXT = '➡️ بعدی'

BT_FAS_BACK = '⬅️ قبلی'

#Button dictionary

BUTTONS = {
        'en': {
            'Language' : BT_EN_LANGUAGE,
            'Help' : BT_EN_HELP,
            'Show_files' : BT_EN_SHOW_FILES,
            'Compress' : BT_EN_COMPRESS,
            'Cancel_compression' : BT_EN_CANCEL_COMPRESSION,
            'Encrypt' : BT_EN_ENCRYPT,
            'Dont_encrypt' : BT_EN_DONT_ENCRYPT,
            'Remove_files': BT_EN_REMOVE_FILES,
            'Next': BT_EN_NEXT,
            'Back': BT_EN_BACK,
            },
        'fas': {
            'Language' : BT_FAS_LANGUAGE,
            'Help' : BT_FAS_HELP,
            'Show_files' : BT_FAS_SHOW_FILES,
            'Compress' : BT_FAS_COMPRESS,
            'Cancel_compression' : BT_FAS_CANCEL_COMPRESSION,
            'Encrypt' : BT_FAS_ENCRYPT,
            'Dont_encrypt' : BT_FAS_DONT_ENCRYPT,
            'Remove_files': BT_FAS_REMOVE_FILES,
            'Next': BT_FAS_NEXT,
            'Back': BT_FAS_BACK,
            },
        }

#Button dict function

def get_button_name (lang: str, key: str):
    Bt_dict = BUTTONS.get (lang, 'en')

    return Bt_dict.get(key, key)

