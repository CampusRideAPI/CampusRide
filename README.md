# Getting Started with Our Project

## Prerequisites
- Git installed on your computer
- Python 3.x installed
- Your GitHub account added to the project

## Initial Setup

### 1. Clone the Repository
```bash
# Open terminal/command prompt and navigate to where you want the project
cd your/preferred/location

# Clone the repository
git clone [repository-URL]
cd [project-name]
```

### 2. Set Up Your Development Environment

#### Windows:
```bash
# Create a virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Mac/Linux:
```bash
# Create a virtual environment
python -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Working on Features

### 1. Create a Feature Branch
Always create a new branch when working on a feature:
```bash
# Make sure you're on main and it's up to date
git checkout main
git pull

# Create and switch to a new feature branch
git checkout -b feature/your-feature-name
```

Branch naming convention:
- Use `feature/` prefix
- Use descriptive names in kebab-case
- Examples:
  - `feature/add-login-page`
  - `feature/fix-database-connection`
  - `feature/update-user-profile`

### 2. Making Changes
```bash
# Check what files you've changed
git status

# Add your changes
git add filename.py
# OR add all changes
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
5. Add description of your changes
6. Create pull request

## Running the Project

### Start the Backend:
```bash
# Make sure you're in the project directory and virtual environment is activated
cd backend
uvicorn main:app --reload
```
Backend will run at: http://localhost:8000

### Start the Frontend:
```bash
# In a new terminal, activate virtual environment
cd frontend
flask run
```
Frontend will run at: http://localhost:5000

## Common Issues and Solutions

### "ModuleNotFoundError"
- Make sure virtual environment is activated
- Run `pip install -r requirements.txt` again

### Git Issues
1. "Cannot push to remote":
```bash
# Pull latest changes first
git pull origin main
# Try pushing again
git push origin your-branch-name
```

2. "Wrong branch":
```bash
# Check current branch
git branch
# Switch to correct branch
git checkout correct-branch
```

## Tips for Successful Development
1. Always pull latest changes before creating new branch
2. Keep commits small and focused
3. Write clear commit messages
4. Test your changes before pushing
5. Ask for help if you're stuck!

## Project Structure
```
project/
├── backend/            # FastAPI backend
│   ├── main.py
│   └── requirements.txt
├── frontend/           # Flask frontend
│   ├── app.py
│   └── requirements.txt
└── README.md
```

## Need Help?
- Check project documentation
- Ask in team chat
- Create an issue on GitHub
- Ask during team meetings

Remember: No question is too simple to ask! We're all here to learn and help each other.
