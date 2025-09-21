#!/bin/bash

# Build the project
echo "Building the project..."
mkdir staticfiles
python3 -m ensurepip
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Apply database migrations
echo "Making Migrations..."
python3 manage.py makemigrations
python3 manage.py migrate

echo "Collecting Static Files..."
python3 manage.py collectstatic

echo "Vercel build process completed."