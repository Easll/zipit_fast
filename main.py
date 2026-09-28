import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, filters
from telegram.ext.filters import BaseFilter
from handlers.start import start, help, show_lang, inline_start
from handlers.zip import ASKING_FOR_ARCHIVE_NAME, ASKING_FOR_ENCRYPTION, ASKING_FOR_PASSWORD, ask_for_password, get_files, add_files, ask_for_archive_name, ask_for_password, inline_compression_flow, inline_start_compression, recive_archive_name, build_archive_encrypted, build_archive_un_encrypted, cancel_compression, inline_show_files, inline_cancel_compression, show_remove_buttons, inline_remove_file, inline_show_remove_buttons
import asyncio
from database import Database
from handlers.proxy import compress_proxy
from utils import find_proxy_url

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
DB_PATH = os.getenv("ZIP_IT_FAST_DB_PATH")
TMP_PATH = os.getenv("ZIP_IT_FAST_TMP_PATH")

async def init_db (app : Application):
    db = Database(DB_PATH)
    await db.init()
    app.bot_data['db'] = db

async def close_db (app : Application):
    db = app.bot_data.get('db')
    if db:
        await db.close()
        print ('Database connection closed')


class _HasProxyFilter(BaseFilter):
    """True when a message's text, caption, or any link entity holds a proxy URL.

    ``filters.Regex`` (used previously) only inspects ``message.text``. Telegram
    stores the destination of a hyperlink in a ``MessageEntity.TEXT_LINK`` entity,
    not in the text, so a labeled proxy link (e.g. ``[label](t.me/proxy?...)``)
    used to slip past the handler. This filter scans those entities too.
    """

    def filter(self, update):
        message = (
            update.channel_post
            or update.message
            or update.edited_channel_post
            or update.edited_message
            or update.business_message
            or update.edited_business_message
            or update.guest_message
        )
        if message is None:
            return False

        text = message.text or message.caption
        entities = message.entities or message.caption_entities or ()
        return find_proxy_url(text, entities) is not None


text_or_caption_has_proxy = _HasProxyFilter()


def main():
    app = Application.builder().token(TOKEN).post_init(init_db).post_shutdown(close_db).build()
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('language', show_lang))

    app.add_handler(CallbackQueryHandler(inline_start, pattern='^start_'))
    app.add_handler(CallbackQueryHandler(inline_show_files, pattern= '^zipnoconv_'))
    app.add_handler(CallbackQueryHandler(inline_remove_file, pattern= '^zipremove:'))
    app.add_handler(CallbackQueryHandler(inline_show_remove_buttons, pattern='^zipremovepage:'))

    app.add_handler(CommandHandler('show_files', get_files))
    app.add_handler(CommandHandler('remove_files', show_remove_buttons))

    app.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('compress', ask_for_archive_name),
            CallbackQueryHandler(inline_start_compression, pattern='^zipstartconv')
            ],
        states={
            ASKING_FOR_ARCHIVE_NAME:[MessageHandler(filters.TEXT & ~filters.COMMAND, recive_archive_name),],
            ASKING_FOR_ENCRYPTION:[
                CommandHandler('encrypt', ask_for_password),
                CommandHandler('dont_encrypt', build_archive_un_encrypted),
                CallbackQueryHandler(inline_compression_flow, pattern= '^zipconv_'),
                ],
            ASKING_FOR_PASSWORD:[MessageHandler(filters.TEXT & ~filters.COMMAND, build_archive_encrypted),]
            },
        fallbacks=[
            CommandHandler('cancel', cancel_compression),
            CallbackQueryHandler(inline_cancel_compression, pattern= '^zipcancelconv_')
            ]
        )) 

    app.add_handler(MessageHandler(filters.ATTACHMENT, add_files))
    app.add_handler(MessageHandler(filters.TEXT & text_or_caption_has_proxy & ~filters.COMMAND, compress_proxy))


    app.run_polling()


if __name__ == "__main__":
    main()
