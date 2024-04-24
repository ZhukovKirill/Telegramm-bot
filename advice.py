from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from config import *
import sqlite3


async def advice(update: Update, context):
    number, name, advice, image = get_advice()
    text = ADVICE_TEXT % (number, name, advice)
    if image is None:
        await update.message.reply_html(text)
    else:
        await update.message.reply_photo(image,
                                         caption=text,
                                         parse_mode='html')


def get_advice():
    connection = sqlite3.connect('db.sqlite')
    cursor = connection.cursor()

    request = '''SELECT tasks.number, tasks.name, advices.advice, advices.image
FROM advices
INNER JOIN tasks
ON tasks.id = advices.task
ORDER BY random()'''
    response: list = cursor.execute(request).fetchone()
    connection.close()
    return response


advice_handler = MessageHandler(filters.Regex(f"^{START_ADVICE_BUTTON}$"), advice)
