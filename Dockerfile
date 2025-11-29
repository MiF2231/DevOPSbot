# Базовый образ с Python
FROM python:3.11-slim
# Указываем рабочую директорию внутри контейнера
WORKDIR /app
# Копируем файл зависимостей
COPY requirements.txt /app/
# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt
# Копируем остальной код в контейнер
COPY . /app
# Команда по умолчанию для запуска бота
CMD ["python", "bot.py"]
