import logging
import firebase_admin
from firebase_admin import credentials, firestore
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.executor import start_polling
from flask import Flask
import threading
import os

# 🔹 Render uchun Flask server
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# 🔹 Bot tokeni
BOT_TOKEN = os.getenv("BOT_TOKEN", "8164935831:AAG10smeIKZd30DuABSDc_f5sxshvVoFpmg")

# 🔹 Firebase sozlamalari
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-adminsdk.json")  # Firebase faylini yuklash
    firebase_admin.initialize_app(cred)
db = firestore.client()

# 🔹 Bot va Dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# 🔹 /start buyrug‘iga javob
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup()

    play_game_button = InlineKeyboardButton(
        text="👋 Play Game", 
        web_app=types.WebAppInfo(url="https://qodextoken-token.vercel.app")
    )

    join_community_button = InlineKeyboardButton(
        text="💪💋 Join Community", 
        url="https://t.me/QODEX_COIN"
    )

    keyboard.add(play_game_button)
    keyboard.add(join_community_button)

    await message.reply("👋 Salom! O‘yin yoki jamiyatga qo‘shiling!", reply_markup=keyboard)

# 🔹 Botni alohida thread'da ishga tushirish
def run_bot():
    logging.basicConfig(level=logging.INFO)
    start_polling(dp, skip_updates=True)

threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))