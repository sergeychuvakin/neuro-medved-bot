import logging

import os
import logging
from config import Config

from telegram import (
    ForceReply,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
    KeyboardButton,
)
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    Filters,
    MessageHandler,
    Updater,
)

from generate_text import generate_n_words, device

# from telegram import *
# from telegram.ext import *
# from requests import *


def test_outside_fun(message):

    if message == "help":
        return Config.HELP_MESSAGE

    
    output = generate_n_words(
        lenght_of_sentence=Config.NUMBER_OF_WORDS, 
        start_sentence=message, 
        device=device
        )

    answer = f"Вы выбрали: {message}\nДмитирий Анатольевич сказал бы так:\n{output}"
    return answer


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# тут всё зависит от скобочек - сколько кнопок в строку [[be],[be]] или [[ be, be],[ be,be ]]
def start_with_key(update: Update, context: CallbackContext):
    buttons = [
        [KeyboardButton(phrase)] for phrase in Config.PRESET_PHARASES
        ]

    context.bot.send_message(
        text="Выберите один из вариантов, а бот продолжил фразу.",
        chat_id=update.effective_chat.id,  # нам надо?
        reply_markup=ReplyKeyboardMarkup(buttons),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text("ничего такого")


def medvo(update: Update, context: CallbackContext) -> None:
    var = update.message.text
    update.message.reply_text(test_outside_fun(var))


def error(update, context):
    #  оно надо?
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # updater = Updater(token)
    updater = Updater(Config.TG_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler("start", start))
    # on non command i.e message
    # dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, medvo))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_error_handler(error)

    # BUTTONS
    dispatcher.add_handler(CommandHandler("start", start_with_key))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, medvo))

    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
