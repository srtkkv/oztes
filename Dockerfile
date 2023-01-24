FROM python:3.11-slim
MAINTAINER SRTKKV <kovalenkokv@gmail.com>
ENV DB_NAME = $DB_NAME
ENV DB_HOST = $DB_HOST
ENV DB_USER = $DB_USER
ENV DB_PASS = $DB_PASS
RUN adduser myuser
RUN pip install --upgrade pip
USER myuser
ENV PROJECT_ROOT /app
WORKDIR $PROJECT_ROOT
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./oztes/ .
CMD python manage.py runserver 0.0.0.0:8000