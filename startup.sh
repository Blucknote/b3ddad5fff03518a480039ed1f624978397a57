#!bin/sh
python3 ./manage.py runserver 0.0.0.0:8000 & celery -A charts worker -l info