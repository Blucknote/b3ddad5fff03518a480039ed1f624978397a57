FROM python:3.5-alpine

RUN apk update
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev
RUN apk add freetype-dev
RUN apk add postgresql-dev
RUN apk add libjpeg-turbo-dev

RUN mkdir -p /home/www/alytics

WORKDIR /home/www/alytics

COPY ./ .

RUN pip3 install -r ./requirements.txt
