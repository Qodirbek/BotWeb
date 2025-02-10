import logging
import firebase_admin
from firebase_admin import credentials, firestore
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

# 🔹 Bot tokeni
BOT_TOKEN = "8164935831:AAG10smeIKZd30DuABSDc_f5sxshvVoFpmg"

# 🔹 Firebase sozlamalari (Agar kerak bo‘lsa)
FIREBASE_CONFIG = {
    "apiKey": "AIzaSyCKWeAIWQcrZlb5toflCu2cll186_HtQPs",
    "authDomain": "qodextoken.firebaseapp.com",
    "projectId": "qodextoken",
    "storageBucket": "qodextoken.firebasestorage.app",
    "messagingSenderId": "582834983319",
    "appId": "1:582834983319:web:526c99d58290264906b4d2"
}

# 🔹 Firebase ulash (Agar kerak bo‘lsa)
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-adminsdk.json")  # Faylni yuklash
    firebase_admin.initialize_app(cred)
db = firestore.client()

# 🔹 Bot va Dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# 🔹 /start buyrug‘iga javob
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup()

    # 👋 Play Game tugmasi (Web App)
    play_game_button = InlineKeyboardButton(
        text="👋 Play Game", 
        web_app=types.WebAppInfo(url="https://qodextoken-token.vercel.app")  # SAYT MANZILI
    )

    # 💪💋 Join Community tugmasi (Telegram kanalga o'tish)
    join_community_button = InlineKeyboardButton(
        text="💪💋 Join Community", 
        url="https://t.me/QODEX_COIN"
    )

    keyboard.add(play_game_button)
    keyboard.add(join_community_button)

    await message.reply("👋 Salom! O‘yin yoki jamiyatga qo‘shiling!", reply_markup=keyboard)

# 🔹 Botni ishga tushirish
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)