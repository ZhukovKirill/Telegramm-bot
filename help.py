from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from config import *


async def help(update: Update, context):
    await update.message.reply_html("""заглушка для вопроса модераторам""")


help_handler = MessageHandler(filters.Regex(f"^{START_HELP_BUTTON}$"), help)