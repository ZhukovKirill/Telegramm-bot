BOT_TOKEN = "6610138819:AAFGqNgeJNM25wE2vI2kXpmVbPpBNhV2JCs"
ANTON_USERNAME = "itsmakrinok"
KIRILL_USERNAME = "Polya_top"
ANTON_ID = "933333468"
KIRILL_ID = "870857071"

START_TEXT = """<b>Привет, друг</b> 👋
Я бот для подготовки к <i>ОГЭ по информатике 2024</i> 😎
Чем могу быть полезен?"""

START_ADVICE_BUTTON = "Дай совет 💡"
START_HELP_BUTTON = "Вопрос модераторам 🆘"
START_EXERCISE_BUTTON = "Случайное задание 🎲"
START_INFO_BUTTON = "Расскажи о заданиях 📖"

START_BUTTONS = [[START_ADVICE_BUTTON, START_EXERCISE_BUTTON],
                 [START_INFO_BUTTON, START_HELP_BUTTON]]

HELP_TEXT_START = """<b>Нужна помощь? 🆘</b>
Отправь сообщение и его увидят модераторы:
<i>Для отмены напиши /stop</i>"""
HELP_TEXT_ASK = """<i>Вопрос успешно отправлен!</i> ✅"""
HELP_TEXT_STOP = """<i>Отправка вопроса отменена!</i> ✅"""
HELP_TEXT_REPLY = """<b>ВОПРОС ОТ ПОЛЬЗОВАТЕЛЯ %s:</b>
    
\"%s\"

<i>Ответь на это сообщение чтобы ответить на вопрос</i>"""
HELP_TEXT_ANSWER = """<b>Твой вопрос:</b>
\"%s\"

<b>Ответ от модератора</b>:
\"%s\""""

OTHER_TEXT = """<i>Простите, но я не понимаю</i> ☹️"""

ADVICE_TEXT = """<b>Совет? Советы это хорошо... Вот тебе один: 💡</b>

Задание №%s: %s

<i>%s</i>"""

INFO_TEXT = """📖 Задание №%s: %s 📖

<i>%s</i>"""