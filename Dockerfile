FROM python:3.5-alpine

RUN apk update
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev 
RUN apk add postgresql-dev zlib-dev libjpeg-turbo-dev

RUN mkdir -p /home/www/graphs

WORKDIR /home/www/graphs

COPY ./ .

RUN pip3 install -r ./requirements.txt
