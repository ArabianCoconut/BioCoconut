import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import *
import Modules.Bio_sequencer as Bio

TOKEN = os.getenv('TOKEN')
load_dotenv()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot_text = "I'm a bot, Created by Arabian Coconut\nMade to do Biological computations"
    user = update.message.from_user.full_name
    await context.bot.send_message(chat_id=update.effective_chat.id, text=bot_text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Welcome {user}!")


async def sequencer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = 'Enter Sequences Followed by space and Mode(Local, Global)\nExample: ATCG ATCG global'
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
    app.updater.start_webhook(
        listen="0.0.0.0",
        port=int(5000),
        url_path=TOKEN,
        webhook_url=f'https://telegram-2dfi.onrender.com/{TOKEN}'
    )

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('sequencer', sequencer))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, sequence_handle))
    app.run_polling(5)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.info('Starting Bot')
