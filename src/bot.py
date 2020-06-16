from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from src.config.auth import token
import subprocess
import logging
TOKEN = token
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('DuditoBot')


def start(update, context):
    logger.info('He recibido un comando start')
    update.message.reply_text("Hola soy un bot,.-.")


def whoami(update, context):
    logger.info("procesando...")
    update.message.reply_text(subprocess.getoutput(["whoami"]))



def free(update, context):
    logger.info("procesando...")
    update.message.reply_text(subprocess.getoutput(["free"]))


def ping(update, context):
    logger.info("procesando...")
    update.message.reply_text(subprocess.getoutput(["ping 8.8.8.8 -c 4"]))


def last(update, context):
    logger.info("procesando...")
    update.message.reply_text(subprocess.getoutput(["last -5 -F"]))


def top(update, context):
    logger.info("procesando...")
    update.message.reply_text(subprocess.getoutput(["top -b -n 1 | head -n 15"]))


def uptime(update, context):
    logger.info("procesando...")
    update.message.reply_text(subprocess.getoutput(["uptime"]))


def firewall(update, context):
    logger.info('He recibido un comando start')
    update.message.reply_text(subprocess.getoutput(["systemctl status firewalld"]))


def ifconfig(update, context):
    logger.info("procesando...")
    update.message.reply_text(subprocess.getoutput(["ifconfig"]))


def w(update, context):
    logger.info("procesando...")
    update.message.reply_text(subprocess.getoutput(["w"]))


def health_apache(update, context):
    logger.info("procesando...")
    update.message.reply_text(subprocess.getoutput(["/home/centos/bottelegram/obtenerEstado.sh apache"]))


def health_flask(update, context):
    logger.info("procesando...")
    update.message.reply_text(subprocess.getoutput(["/home/centos/bottelegram/obtenerEstado.sh flask"]))


def mensajeR(update, context):
    logger.info("procesando..")
    if update.message.text.lower() == "adios":
        update.message.reply_text("Hasta la proxima")
    print(update.message.text)


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('whoami', whoami))
    dispatcher.add_handler(CommandHandler('free', free))
    dispatcher.add_handler(CommandHandler('ping', ping))
    dispatcher.add_handler(CommandHandler('last', last))
    dispatcher.add_handler(CommandHandler('top', top))
    dispatcher.add_handler(CommandHandler('uptime', uptime))
    dispatcher.add_handler(CommandHandler('firewall', firewall))
    dispatcher.add_handler(CommandHandler('ifconfig', ifconfig))
    dispatcher.add_handler(CommandHandler('w', w))
    dispatcher.add_handler(CommandHandler('health_apache', health_apache))
    dispatcher.add_handler(CommandHandler('health_flask', health_flask))
    dispatcher.add_handler(MessageHandler(Filters.text, mensajeR))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()