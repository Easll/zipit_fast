from telegram import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


# under the start message
def get_greet_buttons ():
    keyboard = [
        [
            InlineKeyboardButton(text='🅰 Language | زبان', callback_data='start_language'),
            InlineKeyboardButton(text='🔴 Help | راهنما', callback_data='start_help')
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