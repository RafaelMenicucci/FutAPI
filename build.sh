#!/bin/bash

# Build the project
echo "Building the project..."
python -m pip install -r requirements.txt
python manage.py collectstatic

echo "Vercel build process completed."