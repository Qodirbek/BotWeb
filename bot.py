import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "8164935831:AAG10smeIKZd30DuABSDc_f5sxshvVoFpmg"  # O'zingning bot tokeningni qo'y
WEB_APP_URL = "https://qodextoken.onrender.com/login?start={user_id}"
COMMUNITY_LINK = "https://t.me/QODEX_COIN"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup()
    
    # Play Game tugmasi (Web App)
    play_game_button = InlineKeyboardButton(
        text="👋 Play Game",
        web_app=WebAppInfo(url=WEB_APP_URL.format(user_id=user_id))  # ✅ To‘g‘rilangan
    )
    
    # Join Community tugmasi
    join_community_button = InlineKeyboardButton(
        text="💪💋 Join Community", url=COMMUNITY_LINK
    )

    keyboard.add(play_game_button)
    keyboard.add(join_community_button)

    bot.send_message(
        message.chat.id, 
        f"Welcome, {first_name}! 👋\nClick the button below to start playing.", 
        reply_markup=keyboard
    )

if __name__ == "__main__":
    bot.polling()