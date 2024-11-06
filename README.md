# Getting Started with CampusRide

## Prerequisites

- Git installed on your computer
- Python 3.x installed
- Your GitHub account added to the project

## Initial Setup

### 1. Clone the Repository

```bash
# Clone the repository
git clone https://github.com/CampusRideAPI/CampusRideAPI
cd CampusRideAPI
```

### 2. Set Up Development Environment

#### Windows:

```bash
# Backend setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Frontend setup (in new terminal)
cd frontend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### Mac/Linux:

```bash
# Backend setup
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend setup (in new terminal)
cd frontend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Working on Features

### 1. Create a Feature Branch

```bash
# Make sure you're on main and it's up to date
git checkout main
git pull

# Create and switch to a new feature branch
git checkout -b feature/your-feature-name
```

Branch naming convention:

- Use `feature/` prefix
- Use descriptive names
- Examples:
  - `feature/add-rides`
  - `feature/update-rides`
  - `feature/delete-rides`

### 2. Making Changes

```bash
# Check what files you've changed
git status

# Add your changes
git add .

# Commit your changes
git commit -m "Describe what you changed"

# Push your branch to GitHub
git push origin feature/your-feature-name
```

### 3. Creating a Pull Request

1. Go to GitHub repository
2. Click "Pull requests"
3. Click "New pull request"
4. Select your feature branch
5. Create pull request

## Running the Project

### Start the Backend:

```bash
cd backend
# Make sure venv is activated
uvicorn app.main:app --reload
```

Backend will run at: http://localhost:8000

### Start the Frontend:

```bash
cd frontend
# Make sure venv is activated
flask run
```

Frontend will run at: http://localhost:5000

## Project Structure

```
campusride/
├── api/
│   └── openapi.yaml        # API design document
├── backend/
│   ├── app/
│   │   ├── main.py         # FastAPI app initialization
│   │   ├── models.py       # SQLAlchemy models
│   │   ├── schemas.py      # Pydantic schemas
│   │   ├── database.py     # Database configuration + operations
│   │   └── api.py          # API endpoints
│   └── requirements.txt
├── frontend/
│   ├── app/
│   │   ├── templates/
│   │   │   ├── base.html
│   │   │   ├── index.html
│   │   │   ├── rides_list.html
│   │   │   └── create_ride.html
│   │   ├── static/
│   │   │   └── style.css
│   │   └── app.py
│   └── requirements.txt
└── README.md
```

## Setting Up Database Migrations

First, make sure you're in the backend directory:

```bash
cd backend
```

Initialize Alembic for migrations:

```bash
alembic init alembic
```

Create your first migration:

```bash
alembic revision --autogenerate -m "Initial migration"
```

Run the migrations:

```bash
alembic upgrade head
```

### Common Migration Commands

Create a new migration:

```bash
alembic revision --autogenerate -m "Describe your changes"
```

Apply all pending migrations:

```bash
alembic upgrade head
```

Roll back one migration:

```bash
alembic downgrade -1
```

View migration history:

```bash
alembic history
```

Check current migration version:

```bash
alembic current
```

## Common Issues and Solutions

### ModuleNotFoundError

- Make sure virtual environment is activated
- Run `pip install -r requirements.txt` again

### Git Issues

1. Cannot push to remote:

```bash
git pull origin main
git push origin your-branch-name
```

2. Wrong branch:

```bash
# Check current branch
git branch
# Switch to correct branch
git checkout correct-branch
```

## Tips

1. Always pull latest changes before creating new branch
2. Keep commits small and focused
3. Write clear commit messages
4. Test your changes before pushing
5. Ask for help if needed

## Need Help?

- Ask Aleksi about anything directly
- ?Ask during team meetings?
