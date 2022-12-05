#!/bin/sh
cd /app

while !</dev/tcp/postgres/5432;
    do sleep 3;
done

poetry run ./manage.py migrate
poetry run ./manage.py runserver 0.0.0.0:8000
