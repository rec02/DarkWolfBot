from telegram.ext import Updater, CommanHandler

def start (update, context):

    update.message.replytext('Hola, humano!')

if __name__=='__main__':

    updater = Updater(token='2083176106:AAHRL2aUHoiXVnZC8u-T6bDMnLAxF-Oxvcs', use_context=True)
    dp=updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()