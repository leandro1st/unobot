import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv
from os import environ

# Credentials
load_dotenv('.env')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def echo(update, context):
    """Echo the user message."""
    context.bot.send_message(chat_id='-253417715',
                             text='[uno](tg://user?id=1093071948)', parse_mode="Markdown")


# def callback_minute(context: CallbackContext):
#     context.bot.sendAnimation(chat_id='@fffa343q4',
#                               # that's just data from local gif file
#                               animation='https://c.tenor.com/_bTaLmoLSc4AAAAd/troll-pilled.gif',
#                               caption='[uno](tg://user?id=1093071948)', parse_mode="Markdown")


def callback_minute(context: CallbackContext):
    context.bot.send_message(chat_id='-253417715',
                             text='[uno](tg://user?id=1093071948)', parse_mode="Markdown")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(environ.get('TOKEN'), use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", echo))
    dp.add_handler(CommandHandler("help", echo))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.all, echo))

    j = updater.job_queue
    job_minute = j.run_repeating(callback_minute, interval=60, first=1)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
