
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes


from config import TELEGRAM_BOT_TOKEN



# 1. Define what to do when a message is received
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    print(f"Received from Telegram: {user_text}")
    
    # Optional: Send a response back
    await update.message.reply_text(f"You said: {user_text}")





if __name__ == '__main__':
    # 2. Build the application with your Token
    token = TELEGRAM_BOT_TOKEN
    app = ApplicationBuilder().token(token).build()

    # 3. Add a handler for all text messages
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    # 4. Start the bot (it will wait for messages)
    print("Bot is running...")
    app.run_polling()