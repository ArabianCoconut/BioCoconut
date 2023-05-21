import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import *
import Modules.Bio_sequencer as Bio

load_dotenv()
TOKEN = os.getenv('TOKEN')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot_text = "I'm a bot, Created by Arabian Coconut\nMade to do Biological computations"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=bot_text)


async def sequencer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = 'Enter Sequences Followed by space and mode(Local, Global)\n Example: ATCG ATCG global'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)


async def sequence_handle(update: Update, context: CallbackContext):
    message = update.message.text
    seq1, seq2, mode = message.split(' ')
    Bio.sequence_alignment(seq1, seq2, mode)
    await update.message.reply_text("Alignment Completed Successfully and File is attached")
    await update.message.reply_document(document=open('Modules/alignment.txt', 'rb'))
    os.remove('Modules/alignment.txt')


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('sequencer', sequencer))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, sequence_handle))
    app.run_polling(3)

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.info('Starting Bot')
    main()
