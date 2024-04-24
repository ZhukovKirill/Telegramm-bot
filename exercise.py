from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler, ContextTypes
from config import *
import sqlite3


async def exercise(update: Update, context: ContextTypes.DEFAULT_TYPE):
    markup = ReplyKeyboardMarkup([['/stop']], one_time_keyboard=True, resize_keyboard=True)
    number, name, answer, image = get_exercise()
    context.user_data['answer'] = answer

    text = EXERCISE_TEXT_START % (
        number, name
    )

    await update.message.reply_photo(image,
                                     caption=text,
                                     parse_mode='html',
                                     reply_markup=markup)

    return 1


async def question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answer = context.user_data['answer']
    if answer.lower() in update.message.text.lower():
        markup = ReplyKeyboardMarkup(START_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
        await update.message.reply_html(EXERCISE_TEXT_SUCCESS, reply_markup=markup)
        return ConversationHandler.END
    else:
        await update.message.reply_html(EXERCISE_TEXT_FAIL)
        return 1


def get_exercise():
    connection = sqlite3.connect('db.sqlite')
    cursor = connection.cursor()

    request = '''SELECT tasks.number, tasks.name, exercises.answer, exercises.image
FROM exercises
INNER JOIN tasks
ON tasks.id = exercises.task
ORDER BY random()'''
    response: list = cursor.execute(request).fetchone()
    connection.close()
    return response


async def stop(update: Update, context):
    markup = ReplyKeyboardMarkup(START_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    await update.message.reply_html(EXERCISE_TEXT_STOP % context.user_data['answer'], reply_markup=markup)
    return ConversationHandler.END


exercise_handler = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(f"^{START_EXERCISE_BUTTON}$"), exercise)],

    states={
        1: [MessageHandler(filters.TEXT & ~filters.COMMAND, question)]
    },

    fallbacks=[MessageHandler(filters.COMMAND, stop)]
)

