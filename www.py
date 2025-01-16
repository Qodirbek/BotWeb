from fastapi import FastAPI, Request
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

app = FastAPI()

# Bot tokeningiz
TOKEN = '8164935831:AAEhJMW7D6YdcmPapiNcduwXXdFcknURRus'
bot = Bot(token=TOKEN)
application = Application.builder().token(TOKEN).build()

# Start komandasi uchun tugma
async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Open Web App", web_app={"url": "https://qodextoken.vercel.app"})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome! Press the button below to open the Web App.",
        reply_markup=reply_markup
    )

# Start handlerni botga qo'shish
application.add_handler(CommandHandler("start", start))

@app.post("/")
async def webhook(request: Request):
    # Telegramdan kelgan so'rovlarni qabul qilish
    data = await request.json()
    update = Update.de_json(data, bot)
    await application.process_update(update)
    return {"status": "ok"}

# Vercel uchun asosiy endpoint
@app.get("/")
async def root():
    return {"message": "Bot is running on Vercel!"}