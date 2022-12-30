import logging
from flask import Flask
import logging
from config import Config
import requests

from telegram import (
    ReplyKeyboardMarkup,
    Update,
    KeyboardButton,
)
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    Updater,
)

app = Flask(__name__)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)



# Книпки зависит от скобочек 1 в ряд [[be],[be]] или 2 в ряду[[ be, be],[ be,be ]]
def start_with_key(update: Update, context: CallbackContext):
    buttons = [
        [KeyboardButton(phrase)] for phrase in Config.PRESET_PHARASES_WITH_CONTEXT.keys()
        ]

    context.bot.send_message(
        text="Выберите один из вариантов, а бот продолжил фразу.",
        chat_id=update.effective_chat.id,  # нам надо?
        reply_markup=ReplyKeyboardMarkup(buttons),
    )



def help_command(update: Update, context: CallbackContext) -> None:
    # может положить ссылку на конституцию или сайт правозащитников
    update.message.reply_text('ничего такого')



"""то котики каторые активируются сообщением человека. заменить нутри get_cat() на Медведева"""
def medvo_command(update: Update, context: CallbackContext):
    var = update.message.text
    update.message.reply_text(get_medved(var))


"""вот эту переписать, чтобы ходила не на кошачий сайт а на нейросеть. 
она вернет текст, а та что выше отправит его в чат"""
def get_medved(msg):
    params = {"phrase": msg}

    api_result = requests.get(Config.MODEL_ENDPOINT_URL, params=params)     
    api_response = api_result.json()
    return f"Дмитрий Анатольевич сказал бы так\n{api_response['Dmitro says']}"
    # return f"Дмитрий Анатольевич сказал бы так\n{msg}"


def error(update, context):
    #  оно надо?
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    print(Config.TG_TOKEN)
    updater = Updater(Config.TG_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler("start", start))
    # on non command i.e message
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_error_handler(error)

    # BUTTONS   
    dispatcher.add_handler(CommandHandler("start", start_with_key))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, medvo_command))


    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
