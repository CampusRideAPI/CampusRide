#!/bin/bash

# Create directory structure
mkdir -p api
mkdir -p backend/app
mkdir -p frontend/app/templates
mkdir -p frontend/app/static

# Create empty files
touch api/openapi.yaml
touch backend/app/main.py
touch backend/app/models.py
touch backend/app/schemas.py
touch backend/app/database.py
touch backend/app/crud.py
touch backend/app/errors.py
touch backend/requirements.txt
touch frontend/app/templates/base.html
touch frontend/app/templates/index.html
touch frontend/app/templates/rides_list.html
touch frontend/app/templates/create_ride.html
touch frontend/app/static/style.css
touch frontend/app/app.py
touch frontend/requirements.txt

# Add required Python packages to requirements files
echo "fastapi
uvicorn
sqlalchemy
pydantic" > backend/requirements.txt

echo "flask
requests
python-dotenv" > frontend/requirements.txt

# Make virtual environments and install dependencies
python3 -m venv backend/venv
python3 -m venv frontend/venv

# Activate and install backend dependencies
source backend/venv/bin/activate
pip install -r backend/requirements.txt
deactivate

# Activate and install frontend dependencies
source frontend/venv/bin/activate
pip install -r frontend/requirements.txt
deactivate

echo "Project structure created successfully!"
echo "Next steps:"
echo "1. cd into backend or frontend directory"
echo "2. Activate the virtual environment: source venv/bin/activate"
echo "3. Start coding!"
