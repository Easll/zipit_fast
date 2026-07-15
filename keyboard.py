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



