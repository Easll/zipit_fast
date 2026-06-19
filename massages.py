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


#The dictionary


MESSAGES = {
    'en': {
        'Welcome' : EN_WELCOME,
        'Help' : EN_HELP,
        'Show_lang' : EN_SHOW_LANG,
        'Chose_en' : EN_CHOSE_ENG,
    },

    'fas': {
        'Welcome' : FAS_WELCOME,
        'Help' : FAS_HELP,
        'Show_lang' : FAS_SHOW_LANG,
        'Chose_fas' : FAS_CHOSE_FAS,
    }
}


# The dict function

def get_message (lang : str, key: str):
    lang_dict = MESSAGES.get(lang, 'en')

    return lang_dict.get(key, key)