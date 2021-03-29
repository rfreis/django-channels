#!/bin/bash

cd /app

cp chromedriver /usr/local/bin
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000
