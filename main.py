from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enter your bot token / Введите токен вашего бота
TOKEN = 'Your token'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    await update.message.reply_text(f'Your chat_id: {chat_id}')

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == '__main__':
    main()