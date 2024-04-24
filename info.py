from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ContextTypes, CallbackQueryHandler
from config import *
import sqlite3


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [[InlineKeyboardButton("➡️", callback_data="right")]]
    markup = InlineKeyboardMarkup(buttons)

    number, name, description = get_info(1)
    message = await update.message.reply_html(INFO_TEXT % (
        number, name, description
    ), reply_markup=markup)

    context.user_data[message.id] = 1


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.message.message_id not in context.user_data:
        await query.delete_message()
        return
    number = int(context.user_data[query.message.message_id])

    if query.data == "left":
        number -= 1
    elif query.data == "right":
        number += 1

    number = max(1, min(17, number))
    if number != context.user_data[query.message.message_id]:
        if number == 1:
            buttons = [[InlineKeyboardButton("➡️", callback_data="right")]]
        elif number == 17:
            buttons = [[InlineKeyboardButton("⬅️", callback_data="left")]]
        else:
            buttons = [[InlineKeyboardButton("⬅️", callback_data="left"),
                        InlineKeyboardButton("➡️", callback_data="right")]]
        markup = InlineKeyboardMarkup(buttons)
        number1, name, description = get_info(number)
        await query.edit_message_text(INFO_TEXT % (
            number1, name, description
        ), parse_mode="html", reply_markup=markup)

    context.user_data[query.message.message_id] = number


def get_info(number):
    connection = sqlite3.connect('db.sqlite')
    cursor = connection.cursor()

    request = f'''SELECT tasks.number, tasks.name, tasks.description
FROM tasks
WHERE tasks.id = {number}'''
    response: list = cursor.execute(request).fetchone()
    connection.close()
    return response


info_handler = MessageHandler(filters.Regex(f"^{START_INFO_BUTTON}$"), info)
info_buttons_handler = CallbackQueryHandler(button)