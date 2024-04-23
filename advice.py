from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler
import random


async def advice(update: Update, context):
    await update.message.reply_html("""<b>Совет? Советы это хорошо... Вот тебе один:</b>""")

