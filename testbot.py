from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Tokeningizni shu yerga kiriting
BOT_TOKEN = "8164935831:AAEhJMW7D6YdcmPapiNcduwXXdFcknURRus"

# Start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # WebApp tugmasi
    webapp_button = KeyboardButton(
        text="Open WebApp",
        web_app=WebAppInfo(url="https://qodextoken.vercel.app")  # O'zingizning URL'ingizni kiriting
    )
    # Klaviatura sozlamasi
    reply_markup = ReplyKeyboardMarkup(
        [[webapp_button]],  # Tugmalarni matritsa shaklida joylashtirish
        resize_keyboard=True,
        one_time_keyboard=False  # Tugma doimiy qoladi
    )
    await update.message.reply_text(
        "Salom! WebApp tugmasini bosib ko'ring:",
        reply_markup=reply_markup
    )

# Asosiy qism
if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # /start komandasi handler
    application.add_handler(CommandHandler("start", start))

    # Botni ishga tushirish
    application.run_polling()