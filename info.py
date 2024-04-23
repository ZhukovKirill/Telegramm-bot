from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from config import *


async def info(update: Update, context):
    await update.message.reply_html("""заглушка для рассказа о заданиях""")


info_handler = MessageHandler(filters.Regex(f"^{START_INFO_BUTTON}$"), info)