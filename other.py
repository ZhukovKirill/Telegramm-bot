from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from config import *


async def other(update: Update, context):
    markup = ReplyKeyboardMarkup(START_BUTTONS, one_time_keyboard=False)
    await update.message.reply_html(OTHER_TEXT, reply_markup=markup)


other_handler = MessageHandler(filters.TEXT, other)