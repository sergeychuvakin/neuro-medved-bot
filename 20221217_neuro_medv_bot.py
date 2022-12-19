import os
import logging
from config import Config

from telegram import ForceReply, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    Filters,
    MessageHandler,
    Updater,
)

from generate_text import  generate_n_words, device


def test_outside_fun(message):
    """" Медведящая функция тут """

    output = generate_n_words(
        lenght_of_sentence=Config.NUMBER_OF_WORDS, 
        start_sentence=message, 
        device=device
        )

    answer = f"Вы ввели: {message}\nДмитирий Анатольевич сказал бы так:\n{output}"
    return answer




token = os.getenv("TG_TOKEN")
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and context.
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Ты пишешь начало предложения, сеть нейро-Медведев дописывает продолжение поста. Начинай"
    )


# Можем по имени звать юзера, но наверное не надо ничего личного

# def start(update: Update, context: CallbackContext) -> None:
#     """Send a message when the command /start is issued."""
#     user = update.effective_user
#     update.message.reply_markdown_v2(
#         fr'Здарова {user.mention_markdown_v2()}, отправьте начало предложения, нейро\-Медведев продолжит его за вас\.'
#         , reply_markup=ForceReply(selective=False),
#         # update.message.reply_text('Ты пишешь начало предложения, сеть нейро-Медведев дописывает продолжение поста. Начинай')
#     )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text("ничего такого")


def medvo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    # update.message.reply_text(update.message.text)

    # var = 'щас'
    var = update.message.text
    update.message.reply_text(test_outside_fun(var))
    # print(var,var)
    # return update.message_to_medv


def error(update, context):
    #  оно надо?
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # updater = Updater(token)
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, medvo))
    dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
