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
            InlineKeyboardButton(text= get_button_name(lang = lang, key = 'Show_files'), callback_data='zipnoconv_show_files:0:0'),
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
def get_pending_files_buttons (lang: str, next_page: int | None, pre_page: int | None):
    keyboard = [
            [
                InlineKeyboardButton(text = get_button_name(lang = lang, key = 'Compress'), callback_data= 'zipstartconv'),
                ],
            [
                InlineKeyboardButton(text= get_button_name(lang = lang, key= 'Remove_files'), callback_data= 'zipremovepage_0')]
            ]

    page_buttons = []

    if pre_page != None:
        pre_page_button = InlineKeyboardButton(text=get_button_name(lang=lang, key='Back'), callback_data= f"zipnoconv_show_files:{pre_page}:1")
        page_buttons.append(pre_page_button)

    if next_page:
        next_page_button = InlineKeyboardButton(text= get_button_name(lang= lang, key= 'Next'), callback_data= f"zipnoconv_show_files:{next_page}:1")
        page_buttons.append(next_page_button)

    keyboard.append(page_buttons)


    return InlineKeyboardMarkup(keyboard)

def get_cancel_button (lang: str):
    keyboard = [
            [
                InlineKeyboardButton(text= get_button_name(lang = lang, key = 'Cancel_compression'), callback_data= 'zipcancelconv_cancel_compression'),
                ],
            ]

    return InlineKeyboardMarkup(keyboard)

def get_ask_for_encryption_buttons (lang: str):
    keyboard = [
            [
                InlineKeyboardButton(text= get_button_name(lang = lang, key = 'Encrypt'), callback_data= 'zipconv_encrypt'),
                InlineKeyboardButton(text= get_button_name(lang = lang, key = 'Dont_encrypt'), callback_data= 'zipconv_dont_encrypt'),
                ],
            [
                InlineKeyboardButton(text= get_button_name(lang = lang, key = 'Cancel_compression'), callback_data= 'zipcancelconv_cancel_compression'),
                ],
            ]

    return InlineKeyboardMarkup(keyboard)


def get_remove_buttons (lang: str, files: dict, next_page: None | int , pre_page: None | int):
    buttons = []
    for file in files:
        button = [InlineKeyboardButton(text= f"{file['file_name']}", callback_data= f"zipremove_{file['id']}")]
        buttons.append(button)

    page_buttons = []

    if pre_page != None:
        pre_page_button = InlineKeyboardButton(text=get_button_name(lang=lang, key='Back'), callback_data= f"zipremovepage_{pre_page}")
        page_buttons.append(pre_page_button)

    if next_page:
        next_page_button = InlineKeyboardButton(text= get_button_name(lang= lang, key= 'Next'), callback_data= f"zipremovepage_{next_page}")
        page_buttons.append(next_page_button)

    buttons.append(page_buttons)

    keyboard = buttons
    return InlineKeyboardMarkup(keyboard)
