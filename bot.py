import logging
from telegram.ext import Updater, CommandHandler
from flask import Flask, jsonify, request

# Flask ilovasi yaratish
app = Flask(__name__)

# Telegram bot tokenini kiritish
TOKEN = "8164935831:AAEhJMW7D6YdcmPapiNcduwXXdFcknURRus"  # BotFather'dan olingan token
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Botga start komandasini qo'shish
def start(update, context):
    user_name = update.message.from_user.username
    user_id = update.message.from_user.id
    message = f"Salom {user_name}, bu sizning maxsus havolangiz: https://qodextoken.onrender.com/?user={user_id}"
    update.message.reply_text(message)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Telegram botni boshlash
updater.start_polling()

# Flask ilovasini boshlash
@app.route('/')
def home():
    return jsonify({"message": "Hello, this is your Flask app!"})

if __name__ == '__main__':
    app.run(debug=True)