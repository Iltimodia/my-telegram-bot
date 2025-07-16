# --- v1.1 ---
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import re # Импортируем модуль для работы с регулярными выражениями

# --- Читаем токен из файла ---
try:
    with open("token.txt", "r") as f:
        TOKEN = f.read().strip()
except FileNotFoundError:
    print("Ошибка: Файл token.txt не найден! Создайте файл token.txt и поместите в него токен вашего бота.")
    exit()

# --- Тексты для кнопок ---
# Выносим тексты в переменные, чтобы было удобнее их использовать
BUTTON1_FLIRT = "Освоить искусство идеального флирта💬"
BUTTON2_DESIRE = "Как разжечь в ней безумное желание? ❤️‍🔥"
BUTTON3_PHOTOS = "Открываю пикантные фото и видео 🤫🔥"
BUTTON4_PLAN = "Получить пошаговый план по покорению девушек! ✨"


# --- Функции-обработчики ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Отправляет приветственное сообщение и главное меню.
    """
    # Создаем клавиатуру. Кнопки расположены по две в ряду.
    keyboard = [
        [KeyboardButton(BUTTON1_FLIRT), KeyboardButton(BUTTON2_DESIRE)],
        [KeyboardButton(BUTTON3_PHOTOS), KeyboardButton(BUTTON4_PLAN)],
    ]
    
    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        input_field_placeholder="Выберите один из пунктов меню"
    )

    # Отправляем приветственное сообщение
    await update.message.reply_text(
        "👐Привет, ты попал в бот ErikaLight, выбери с чего хочешь начать наше общение",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправляет сообщение с помощью по командам."""
    await update.message.reply_text(
        "Используйте кнопки меню для навигации.\n\n"
        "Доступные команды:\n"
        "/start - Перезапустить бота и вернуться в главное меню"
    )

# --- Функции для кнопок главного меню ---
# Пока что это просто заглушки, которые подтверждают нажатие

async def handle_flirt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает нажатие на кнопку 'Флирт'."""
    await update.message.reply_text(f"Вы выбрали: '{BUTTON1_FLIRT}'. Этот раздел скоро появится!")

async def handle_desire(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает нажатие на кнопку 'Желание'."""
    await update.message.reply_text(f"Вы выбрали: '{BUTTON2_DESIRE}'. Этот раздел скоро появится!")

async def handle_photos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает нажатие на кнопку 'Фото'."""
    await update.message.reply_text(f"Вы выбрали: '{BUTTON3_PHOTOS}'. Этот раздел скоро появится!")

async def handle_plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает нажатие на кнопку 'План'."""
    await update.message.reply_text(f"Вы выбрали: '{BUTTON4_PLAN}'. Этот раздел скоро появится!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Эта функция будет срабатывать, если пользователь введет текст,
    который не совпадает ни с одной кнопкой или командой.
    """
    await update.message.reply_text(
        "Я не понимаю эту команду. Пожалуйста, используйте кнопки меню.\n\n"
        "Чтобы вернуться в главное меню, введите /start"
        )

def main():
    """Основная функция для запуска бота."""
    application = Application.builder().token(TOKEN).build()

    # --- Добавляем обработчики ---
    
    # Команды
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    # Кнопки меню
    # Используем re.escape, чтобы специальные символы (?, 🔥) не ломали фильтр
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex(f"^{re.escape(BUTTON1_FLIRT)}$"), handle_flirt))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex(f"^{re.escape(BUTTON2_DESIRE)}$"), handle_desire))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex(f"^{re.escape(BUTTON3_PHOTOS)}$"), handle_photos))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex(f"^{re.escape(BUTTON4_PLAN)}$"), handle_plan))

    # Эхо-ответ (срабатывает на любой другой текст)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запускаем бота
    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()