from telegram import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


# under the start message
def get_greet_buttons ():
    keyboard = [
        [
            InlineKeyboardButton(text='🅰 Language | زبان', callback_data='/language'),
            InlineKeyboardButton(text='🔴 Help | راهنما', callback_data='/help')
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
