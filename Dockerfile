FROM python:3.10-slim-buster

ENV PYTHONBUFFERED=1

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt --no-cache

COPY src src

