from fastapi import FastAPI
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

app = FastAPI()

TOKEN = '8164935831:AAEhJMW7D6YdcmPapiNcduwXXdFcknURRus'  # Bot tokeningiz

# Telegram botini sozlash
application = Application.builder().token(TOKEN).build()

# /start komandasi uchun handler
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Open Web App", url="https://qodextoken.vercel.app")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome! Click the button below to open the Web App.", reply_markup=reply_markup
    )

# Telegram bot uchun handler qo'shish
application.add_handler(CommandHandler("start", start))

@app.on_event("startup")
async def on_startup():
    # Telegram botni polling rejimida ishga tushirish
    import asyncio
    asyncio.create_task(application.run_polling())

@app.get("/")
async def root():
    return {"message": "Bot is running and ready!"}