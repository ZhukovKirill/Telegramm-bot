from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from config import *


async def advice(update: Update, context):
    await update.message.reply_html("""<b>Совет? Советы это хорошо... Вот тебе один:</b>""")


advice_handler = MessageHandler(filters.Regex(f"^{START_ADVICE_BUTTON}$"), advice)
