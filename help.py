from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler, ContextTypes
from config import *


async def help(update: Update, context):
    markup = ReplyKeyboardMarkup([['/stop']], one_time_keyboard=True)
    await update.message.reply_html(HELP_TEXT_START, reply_markup=markup)
    return 1


async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    markup = ReplyKeyboardMarkup(START_BUTTONS, one_time_keyboard=False)
    await update.message.reply_html(HELP_TEXT_ASK, reply_markup=markup)

    await context.bot.send_message(ANTON_ID, HELP_TEXT_REPLY % (
        update.effective_user.id,
        update.message.text
    ), parse_mode="html")
    await context.bot.send_message(KIRILL_ID, HELP_TEXT_REPLY % (
        update.effective_user.id,
        update.message.text
    ), parse_mode="html")

    return ConversationHandler.END


async def stop(update: Update, context):
    markup = ReplyKeyboardMarkup(START_BUTTONS, one_time_keyboard=False)
    await update.message.reply_html(HELP_TEXT_STOP, reply_markup=markup)
    return ConversationHandler.END


# help_handler = MessageHandler(filters.Regex(f"^{START_HELP_BUTTON}$"), help)

help_handler = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(f"^{START_HELP_BUTTON}$"), help)],

    states={
        1: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask)]
    },

    fallbacks=[MessageHandler(filters.COMMAND, stop)]
)
