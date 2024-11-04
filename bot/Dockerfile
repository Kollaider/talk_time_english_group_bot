# Используем базовый образ Python
FROM python:3.11-slim

WORKDIR /bot

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копируем приложение
COPY bot/ .

# Запускаем aiogram бота
CMD ["python", "main.py"]
