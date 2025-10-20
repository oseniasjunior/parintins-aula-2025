FROM python:3.13.0-slim

RUN apt-get update && apt-get install -y \
    python3-dev

WORKDIR /usr/src/app

COPY . /usr/src/app


RUN pip install --upgrade pip \
    && pip install -r requirements.txt

