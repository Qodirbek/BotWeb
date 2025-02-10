import logging
import firebase_admin
from firebase_admin import credentials, firestore
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.executor import start_polling
from flask import Flask
import threading
import os
import json

# 🔹 Flask server
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# 🔹 Bot tokenini olish
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 🔹 Firebase sozlamalarini `.env` dan olish
firebase_config = {
    "type": os.getenv("FIREBASE_TYPE"),
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace('\\n', '\n'),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.getenv("FIREBASE_CLIENT_ID"),
    "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
    "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL"),
}

# 🔹 Firebase'ni ulash
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_config)  # JSON fayl o'rniga `.env` dan olish
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