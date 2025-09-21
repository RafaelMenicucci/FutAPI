#!/bin/bash

# Build the project
echo "Building the project..."
mkdir staticfiles
python3.10 -m ensurepip
python3.10 -m pip install --upgrade pip
python3.10 -m pip install -r requirements.txt
python3.10 manage.py collectstatic

echo "Vercel build process completed."