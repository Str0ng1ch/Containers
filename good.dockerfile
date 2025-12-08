# Установка минимального образа
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
# Одна команда RUN для установки пакетов + очищение кэша
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Создание юзера с ограниченными правами
RUN useradd -m -u 1000 appuser
USER appuser

VOLUME /app/data

EXPOSE 5000
CMD ["python", "app.py"]