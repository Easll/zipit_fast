from telegram import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from massages import get_button_name

# under the start message
def get_greet_buttons (lang: str):
    keyboard = [
        [
            InlineKeyboardButton(text='🅰 Language | زبان', callback_data='start_language'),
            InlineKeyboardButton(text='🔴 Help ', callback_data='start_help')
        ],
        [
            InlineKeyboardButton(text= get_button_name(lang = lang, key = 'Show_files'), callback_data='zipnoconv_show_files'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

# for choosing languages. under the show_lang
def get_lang_buttons ():
    keyboard = [
        [
            InlineKeyboardButton(text= 'فارسی', callback_data='start_fas'),
            InlineKeyboardButton(text='English', callback_data='start_eng')
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

# under the message that shows pending files
def get_pending_files_buttons (lang: str):
    keyboard = [
            [
                InlineKeyboardButton(text = get_button_name(lang = lang, key = 'Compress'), callback_data= 'zipnoconv_compress'),
                ],
            ]
    return InlineKeyboardMarkup(keyboard)

def get_cancel_button (lang: str):
    keyboard = [
            [
                InlineKeyboardButton(text= get_button_name(lang = lang, key = 'Cancel_compression'), callback_data= 'zipnoconv_cancel_compression'),
                ],
            ]

    return InlineKeyboardMarkup(keyboard)

def get_ask_for_encryption_buttons (lang: str):
    keyboard = [
            [
                InlineKeyboardButton(text= get_button_name(lang = lang, key = 'Encrypt'), callback_data= 'zipnoconv_encrypt'),
                InlineKeyboardButton(text= get_button_name(lang = lang, key = 'Dont_encrypt'), callback_data= 'zipnoconv_dont_encrypt'),
                ],
            [
                InlineKeyboardButton(text= get_button_name(lang = lang, key = 'Cancel_compression'), callback_data= 'zipnoconv_cancel_compression'),
                ],
            ]

    return InlineKeyboardMarkup(keyboard)
