from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler


async def info(update: Update, context):
    await update.message.reply_html("""заглушка для рассказа о заданиях""")
