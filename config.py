import os
BOT_TOKEN = "8207878197:AAFvdw7NJS29Amwmlr5aBqGZ2BX6XFZSVYE"

# Токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN", "ЗАГЛУШКА_ДЛЯ_ЛОКАЛЬНОГО_ТЕСТА")

# Параметры базы данных
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "3307"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "1234")
DB_NAME = os.getenv("DB_NAME", "telegram_bot_db_Kamalov")


