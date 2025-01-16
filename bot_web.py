from fastapi import FastAPI
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, Application, CallbackContext

app = FastAPI()

# Telegram bot tokenini o'zingiznikiga o'zgartiring
TOKEN = "8164935831:AAEhJMW7D6YdcmPapiNcduwXXdFcknURRus"

bot = Bot(token=TOKEN)
application = Application.builder().token(TOKEN).build()

# Start komandasi
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Open Web App", url="https://qodextoken.vercel.app")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to the bot! Click to open the web app.", reply_markup=reply_markup)

# Bot uchun handler qo'shish
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

@app.get("/")
async def root():
    """
    FastAPI endpoint
    """
    application.run_polling(drop_pending_updates=True)
    return {"message": "Bot is running!"}