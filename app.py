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
        "ASSALOMU ALEYKUM ISHINGIZGA HUSH KELIBSIZ BU YERDA KELAJAK UCHUN $QODEX TOKENINI ISHLAYSIZ ISHINGIZGA OMAD:", reply_markup=keyboard
    )

# Bot tokeningizni shu yerga joylang
TOKEN = "8164935831:AAEhJMW7D6YdcmPapiNcduwXXdFcknURRus"

application = Application.builder().token(TOKEN).build()

# /start komandasi uchun handler
application.add_handler(CommandHandler("start", start))

# Botni ishga tushirish
application.run_polling()