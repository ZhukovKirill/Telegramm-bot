from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler
from config import *

from start import start_handler
from advice import advice_handler
from exercise import exercise_handler
from help import help_handler
from info import info_handler


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(start_handler)
    application.add_handler(advice_handler)
    application.add_handler(exercise_handler)
    application.add_handler(info_handler)
    application.add_handler(help_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
