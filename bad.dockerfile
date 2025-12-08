# Все действия делаются под root-ом
# Устанавливаем большой образ (лишнее для данного проекта)
FROM python:3.12

# Делаем RUN в несколько строк -> создание нескольких слоев -> увеличение размера docker образа
RUN apt-get update

# Установка python, хотя он есть в базовом образе
RUN apt-get install -y python3 python3-pip

# Копирование всей папки (может быть плохо, если лежит мусор + нет .dockerignore)
COPY . /app
WORKDIR /app

# Установка без очистки кэша пакетов -> увеличение размера docker образа
RUN pip3 install -r requirements.txt

VOLUME /app/data

EXPOSE 5000
CMD ["python3", "app.py"]