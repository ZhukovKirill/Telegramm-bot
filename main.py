from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler, ContextTypes
from config import *

from start import start_handler
from advice import advice_handler
from exercise import exercise_handler
from help import help_handler
from help_reply import help_reply_handler
from info import info_handler, info_buttons_handler
from other import other_handler


async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.photo[-1].file_id)


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # application.add_handler(MessageHandler(filters.PHOTO, photo))

    application.add_handler(help_handler)
    application.add_handler(help_reply_handler)
    application.add_handler(exercise_handler)
    application.add_handler(start_handler)
    application.add_handler(advice_handler)
    application.add_handler(info_handler)
    application.add_handler(info_buttons_handler)
    application.add_handler(other_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
