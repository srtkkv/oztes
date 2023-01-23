FROM python:3.11-slim
MAINTAINER KKV <kovalenkokv@gmail.com>
RUN adduser myuser
RUN pip install --upgrade pip
USER myuser
ENV PROJECT_ROOT /app
WORKDIR $PROJECT_ROOT
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./oztes/ .
CMD python manage.py runserver 0.0.0.0:8000