FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Компіляція файлів перекладів
RUN pybabel compile -d translations

# Запуск додатку
CMD ["python", "app/app.py"]
