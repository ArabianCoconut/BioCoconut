import logging
import os
from telegram import Update
from telegram.ext import ContextTypes, CallbackContext, CommandHandler, MessageHandler, filters,ApplicationBuilder,Updater
import Modules.Bio_sequencer as Bio

TOKEN = os.getenv('TOKEN')

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

async def secret(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = 'This is a secret message, I dont know what it is!'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('sequencer', sequencer))
    app.add_handler(CommandHandler('secret', secret))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, sequence_handle))
    app.run_polling(2)
    
if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.info('Starting Bot')