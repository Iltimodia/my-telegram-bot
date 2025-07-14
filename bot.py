import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Этот код будет брать токен из настроек сервера (или переменных окружения)
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я эхо-бот, созданный на MacBook и готовый к запуску на Render.")

# Функция, которая будет отвечать тем же сообщением (эхо)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

def main():
    # Создаем объект приложения
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчик для команды /start
    application.add_handler(CommandHandler("start", start))
    # Добавляем обработчик для всех текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запускаем бота
    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()
