from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler  # CallbackQueryHandler ni import qilamiz

TOKEN = '8164935831:AAFRLKMSIQlsoQUpuXN-3iqC2thQOQCOwr4'  # O'zgartiring

async def start(update: Update, context: CallbackContext):
    # Inline tugmalarni yaratish
    keyboard = [
        [InlineKeyboardButton("👋 Play Game", web_app={"url": "https://qodextoken.onrender.com"})],
        [InlineKeyboardButton("💪💋 Join Community", url="https://t.me/QODEX_COIN")],  # Telegram kanaliga o'tish
        [InlineKeyboardButton("🧾 Help", callback_data="help")]  # Help tugmasi
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Foydalanuvchiga xabar yuborish
    await update.message.reply_text("Welcome! Press the button below to open the Web App.", reply_markup=reply_markup)

async def help(update: Update, context: CallbackContext):
    # Yordam xabari
    help_text = """
    Explore the complete guide

    Tap to Earn:
    TapSwap is an addictive clicker game where you accumulate Shares by tapping the screen.

    Leagues:
    Climb the ranks by earning more Shares and outperforming others in the leagues.

    Boosts:
    Unlock boosts and complete tasks to maximize your Shares earnings.

    Friends:
    Invite others and both of you will receive bonuses. Assist your friends in advancing to higher leagues for bigger Shares rewards.

    The Purpose:
    Collect as many Shares as possible and exchange them for QODEX.
    """
    # Yordam xabarini yuborish
    await update.message.reply_text(help_text)

def main():
    application = Application.builder().token(TOKEN).build()

    # Command handler qo'shish
    application.add_handler(CommandHandler("start", start))

    # Callback handler qo'shish (Help tugmasi uchun)
    application.add_handler(CallbackQueryHandler(help, pattern="help"))

    # Pollingni ishga tushirish
    application.run_polling()

if __name__ == '__main__':
    main()