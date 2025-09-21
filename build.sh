#!/bin/bash

# Build the project
echo "Building the project..."
mkdir staticfiles
python -m ensurepip
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py collectstatic

echo "Vercel build process completed."