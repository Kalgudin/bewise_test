FROM python:3.11
RUN apt-get update -y
RUN apt-get upgrade -y


MAINTAINER Nick_Ka

# рабочий каталог
WORKDIR /base

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# устанавливаем postgresql
RUN apt install -y postgresql

# копируем в рабочий каталог
COPY requirements.txt .
# устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# копируем текущий каталог в workdir
COPY . .
# указываем порт(8000 - стандартный django)
EXPOSE 8000
# запускаем сервер
CMD ["python3", "base/manage.py", "runserver", "0.0.0.0:8000"]





