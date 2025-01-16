from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackContext

# WebApp URL
WEB_APP_URL = "https://qodextoken.vercel.app/"

async def start(update: Update, context: CallbackContext):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Play", web_app={'url': WEB_APP_URL}
                )
            ]
        ]
    )
    await update.message.reply_text(
        "Salom! Quyidagi tugma orqali saytga o'tishingiz mumkin:", reply_markup=keyboard
    )

# Bot tokeni
TOKEN = "8164935831:AAEhJMW7D6YdcmPapiNcduwXXdFcknURRus"

application = Application.builder().token(TOKEN).build()

# /start komandasi uchun handler
application.add_handler(CommandHandler("start", start))

# Botni ishga tushiring
application.run_polling()