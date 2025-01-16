from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

# Bot tokeningiz
TOKEN = '8164935831:AAEhJMW7D6YdcmPapiNcduwXXdFcknURRus'

# Start komandasi uchun funksiya
async def start(update: Update, context: CallbackContext):
    # Tugmalarni faqat bir marta ko'rsatish uchun inline klaviatura yaratamiz
    keyboard = [
        [InlineKeyboardButton("Open Web App", url="https://qodextoken.vercel.app")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Foydalanuvchiga xabar va tugmani yuborish
    await update.message.reply_text("Welcome! Click the button below to open the Web App.", reply_markup=reply_markup)

# Asosiy funksiya
def main():
    # Botni ishga tushirish uchun Application obyekti
    application = Application.builder().token(TOKEN).build()

    # Handlerlar qo'shish
    application.add_handler(CommandHandler("start", start))

    # Webhook yoki polling orqali botni ishga tushirish
    application.run_polling()

# Skriptni ishga tushirish
if __name__ == '__main__':
    main()