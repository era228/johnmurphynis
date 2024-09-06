# Базовый образ: используем официальный образ Python версии 3.9
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с кодом нашего приложения в контейнер
COPY quadratic_solver.py /app/quadratic_solver.py

# Устанавливаем необходимые зависимости (sympy для решения уравнений)
RUN pip install sympy

# Определяем команду по умолчанию для запуска приложения
CMD ["python", "quadratic_solver.py"]
