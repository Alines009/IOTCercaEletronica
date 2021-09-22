import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Olá {user.mention_markdown_v2()}\! Insira o comando /monitor para iniciar o monitoramento do veículo ;\)',
        reply_markup=ForceReply(selective=True),
    )

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Este bot notifica o usuário caso o veículo saia da rota.')

def alarm(context: CallbackContext) -> None:
    """Send the alarm message."""

    try:
        f = open("../alert.txt", "r")
        sensor_data = f.read().split("#")
        print(sensor_data)
        f.close()

        if (sensor_data[0] == 'True'):
            job = context.job
            context.bot.send_message(job.context, text= '🚨🚨🚨 ATENÇÃO!!! \nO veículo está fora da rota. Acesse o mapa para verificar a localização atual do veículo.')
            job.schedule_removal()
    except IOError:
        job = context.job
        context.bot.send_message(job.context, text='Sinto muito... \nAinda não temos informações sobre o rastreamento do veículo. \nTente novamente mais tarde.')
        job.schedule_removal()

def set_iniciar(update: Update, context: CallbackContext) -> None:
    """Add a job to the queue."""
    chat_id = update.message.chat_id
    try:
        context.job_queue.run_repeating(alarm, 5, context=chat_id, name=str(chat_id))
        text = 'Monitoramento iniciado com sucesso!'
        update.message.reply_text(text)

    except (IndexError, ValueError):
        update.message.reply_text('Não consegui iniciar o monitoramento :(')

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("TOKEN_TELEGRAM")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("monitor", set_iniciar))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
