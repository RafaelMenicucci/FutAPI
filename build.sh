#!/bin/bash

# Build the project
echo "Building the project..."
mkdir staticfiles
python3.9 -m ensurepip
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic

echo "Vercel build process completed."