#!/bin/sh

sleep 10

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn greatesoft.wsgi:application --bind 0.0.0.0:8000 --reload

exec "$@"
