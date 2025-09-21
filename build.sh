#!/bin/bash

# Build the project
echo "Building the project..."
mkdir staticfiles
python3.11.4 -m ensurepip
python3.11.4 -m pip install --upgrade pip
python3.11.4 -m pip install -r requirements.txt
python3.11.4 manage.py collectstatic

echo "Vercel build process completed."