FROM python:3.5-alpine

RUN apk update
RUN apk add postgresql-dev

RUN mkdir -p /home/www/alytics

WORKDIR /home/www/alytics

COPY ./ .

RUN pip3 install -r ./requirements.txt
