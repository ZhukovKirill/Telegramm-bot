from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler, ContextTypes
from config import *


async def help_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message.text.startswith("ВОПРОС ОТ ПОЛЬЗОВАТЕЛЯ"):
        question_text = update.message.reply_to_message.text
        user = question_text.split()[3][:-1]
        question = question_text[question_text.find('"')+1:question_text.rfind('"')]
        await context.bot.send_message(user, HELP_TEXT_ANSWER % (question, update.message.text), parse_mode="html")


help_reply_handler = MessageHandler(filters.REPLY & (filters.User(username=ANTON_USERNAME) | filters.User(username=KIRILL_USERNAME)), help_reply)
