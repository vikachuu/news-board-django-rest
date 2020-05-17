FROM python:3.7.2

# set environment variables
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

# copy project
COPY . /usr/src/app/

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

