from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from config import *


async def exercise(update: Update, context):
    await update.message.reply_html("""заглушка для задания""")


exercise_handler = MessageHandler(filters.Regex(f"^{START_EXERCISE_BUTTON}$"), exercise)