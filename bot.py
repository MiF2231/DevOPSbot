from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

from config import BOT_TOKEN
from db import save_message, get_last_messages

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
    "Привет! Я обновлённый DevOps CI/CD бот.\n"
    "Я развёрнут через GitHub Actions и Docker."
)


@dp.message(Command("last"))
async def cmd_last(message: types.Message):
    messages = get_last_messages(limit=5)
    if not messages:
        await message.answer("В базе пока нет сообщений.")
        return

    lines = []
    for m in messages:
        user = m["username"] or m["user_id"]
        lines.append(f"{m['created_at']} – {user}: {m['text']}")

    text = "Последние сообщения из базы:\n\n" + "\n".join(lines)
    await message.answer(text)

@dp.message()
async def echo_and_save(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    text = message.text

    # Сохраняем сообщение в базу
    save_message(user_id, username, text)

    # Отвечаем пользователю
    await message.answer(f"Сообщение сохранено в базу: {text}")

async def main():
    print("Бот запущен с поддержкой MySQL...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

