#English messages



EN_WELCOME = """
Hi!

I'm Zipit_Fast!

send me your files and I'll compress them (with encryprion if you want) and send them to you!            

/help for more and /language for setting the language. (supoorting English and Persian at the moment)
"""

EN_HELP = """
Placeholder Text

"""

EN_SHOW_LANG = """
Choose the language 

"""
EN_CHOSE_ENG = """
English was chosen.

You can always set the language from the main menue.

"""


EN_EXTRACTING_MEATDATA = """
Extracting metadata ..."""

EN_METADATA_ADDED = """
Added to your files, ready to be archived:

Name: {name}

Size: {size}
"""

EN_SHOW_PENDING_FILES_I = """
Your pending files:"""

EN_SHOW_PENDING_FILES_II ="""
Name: {name}
Size: {size}
"""

EN_ASKING_FOR_ARCHIVE_NAME ="""
Please enter a name for your archive
"""

EN_ASKING_FOR_ENCRYPTION = """
Do you want your archive to be encrypted?
"""

EN_ASKING_FOR_PASSWORD = """
Please enter a password for your archive
"""

EN_STARTING_COMPRESSION = """
Downloading ..."""

EN_COMPRESSING = """
Compressing ..."""

EN_UPLOADING = """
Uploading ..."""

EN_COMPRESSION_FAILED = """
Compression failed. Please try again.
"""

EN_COMPRESSION_CANCELED = """
Operation canceled."""

EN_NO_PENDING_FILES = """
You have no un-archived files
"""

EN_FILE_TOO_BIG = """
Error: The bot is currently in Test and cannot download files bigger than 20 MB
"""

EN_ARCHIVE_TOO_BIG = """
Error: The total size of your archive will exceed 50 MB. The bot is currently in test and cannot upload files bigget than 50 MB"""
#Farsi messages

FAS_WELCOME = """
سلام!

خوش اومدی!

فایل هات رو برام بفرست تا اونها رو فشرده و ارسال کنم. (امکان رمزگذاری هم هست)

/help برای راهنمایی

/language برای تغییر زبان


"""

FAS_HELP = """
این بخش در حال طراحی است

"""

FAS_SHOW_LANG = """
زبان را انتخاب کنید

"""

FAS_CHOSE_FAS = """
زبان فارسی انتخاب شد.

همیشه می توانید زبان را از منوی اصلی تغییر دهید

"""

FAS_EXTRACTING_MEATDATA ="""
استخراج مشخصات ...""" 

FAS_METADATA_ADDED = """
به فایل های شما افزوده شد. آماده برای فشرده سازی:

نام: {name}

اندازه:{size}
"""

FAS_SHOW_PENDING_FILES_I = """
فایل های آرشیو نشده شما:
"""

FAS_SHOW_PENDING_FILES_II = """
نام: {name}
اندازه: {size}
"""


FAS_ASKING_FOR_ARCHIVE_NAME ="""
لطفا برای آرشیو خود یک نام انتخاب کنید:"""


FAS_ASKING_FOR_ENCRYPTION = """
آیا می خواهید آرشیو شما رمزنگاری شده باشد؟
"""


FAS_ASKING_FOR_PASSWORD = """
لطفا برای آرشیو خود یک رمز انتخاب کنید:"""

FAS_STARTING_COMPRESSION ="""
در حال دانلود ..."""

FAS_COMPRESSING = """
در حال فشرده سازی ..."""

FAS_UPLOADING = """
در حال آپلود ..."""

FAS_COMPRESSION_FAILED = """
فشرده سازی شکست خورد. دوباره تلاش کنید."""

FAS_COMPRESSION_CANCELED = """
عملیات لغو شد."""

FAS_NO_PENDING_FILES = """
فایل آرشیو نشده ای ندارید
"""

FAS_FILE_TOO_BIG = """
مشکل: بات در حال احضر در مرحله تست قرار دارد و نمی تواند فایل های بیشتر از 20 مگابایت را دانلود کند."""

FAS_ARCHIVE_TOO_BIG = """
مشکل: حجم آرشیو شما از 50 مگابایت فراتر رفته است.  بات در حال حاضر در مرحله تست قرار دارد و نمی تواند آرشیو های بیشتر از 50 مگابایت را آپلود کند."""
#The dictionary


MESSAGES = {
    'en': {
        'Welcome' : EN_WELCOME,
        'Help' : EN_HELP,
        'Show_lang' : EN_SHOW_LANG,
        'Chose_en' : EN_CHOSE_ENG,
        'Extracting_metadata': EN_EXTRACTING_MEATDATA,
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
    },

    'fas': {
        'Welcome' : FAS_WELCOME,
        'Help' : FAS_HELP,
        'Show_lang' : FAS_SHOW_LANG,
        'Chose_fas' : FAS_CHOSE_FAS,
        'Extracting_metadata' : FAS_EXTRACTING_MEATDATA,
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
    }
}


# The dict function

def get_message (lang : str, key: str):
    lang_dict = MESSAGES.get(lang, 'en')

    return lang_dict.get(key, key)
