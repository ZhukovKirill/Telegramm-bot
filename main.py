from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from config import *

from start import start
from advice import advice
from exercise import exercise
from help import help
from info import info


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Regex(f"^{START_ADVICE_BUTTON}$"), advice))
    application.add_handler(MessageHandler(filters.Regex(f"^{START_EXERCISE_BUTTON}$"), exercise))
    application.add_handler(MessageHandler(filters.Regex(f"^{START_HELP_BUTTON}$"), help))
    application.add_handler(MessageHandler(filters.Regex(f"^{START_INFO_BUTTON}$"), info))

    application.run_polling()


if __name__ == "__main__":
    main()
