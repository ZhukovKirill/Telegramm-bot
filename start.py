from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from config import *


async def start(update: Update, context):
    markup = ReplyKeyboardMarkup(START_BUTTONS, one_time_keyboard=False)
    await update.message.reply_html(START_TEXT, reply_markup=markup)