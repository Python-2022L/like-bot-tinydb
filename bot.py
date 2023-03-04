from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
import os 

TOKEN=os.environ.get("TOKEN")

def start(update: Update, context: CallbackContext) -> None:
    bot = context.bot
    chat_id = update.message.chat.id

    # likeDB.add_student(str(chat_id))
    bot.sendMessage(chat_id,'Sen me picture!')

updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()