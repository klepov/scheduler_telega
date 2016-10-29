from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

from core import get_scheduler

timestamp = {'сегодня': 1,
             'завтра': 2,
             'все':3}

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('Дратути')


def help(bot, update):
    update.message.reply_text('Команды -'
                              '\nсегодня - выводит пары на сегодня'
                              '\nзавтра - выводит пары на завтра'
                              '\nвсе - выводит все пары недели')


def echo(bot, update):
    update.message.reply_text(parse(update.message.text))


def parse(text):
    text = str(text).lower()
    choose = timestamp.get(text)
    if choose is not None:
        return get_scheduler(choose)
    else:
        return 'чет не понял'


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("242178565:AAFd9JAqiy3d0NHGCVcYOX2L6kvNoJzeK_4")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


main()
