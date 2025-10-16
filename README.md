# Daily Task Tracker

A simple Flask-based web application for managing daily tasks.

## Live Demo

**Hosted App:** https://daily-task-tracker-o6ty.onrender.com/

**GitHub Repository:** https://github.com/rameeshap102/daily_task_tracker

## Features

- Add, edit, and delete daily tasks
- Mark tasks as completed
- View all tasks in a list
- SQLite database for data storage
- Calendar-based date selection
- Dark/Light mode toggle

## How to Run the Project Locally

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository:**

git clone https://github.com/rameeshap102/daily_task_tracker.git

cd daily_task_tracker


2. **Create and activate virtual environment:**

On Windows
python -m venv venv
venv\Scripts\activate

On macOS/Linux
python3 -m venv venv
source venv/bin/activate


3. **Install dependencies:**

pip install -r requirements.txt


4. **Run the application:**

python app.py

5. **Open in browser:**

http://localhost:5000


## Platform Used for Hosting

**Hosting Platform:** Render (Free Tier)

**Deployment Configuration:**
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- Runtime: Python 3

## Difficulties Faced

### 1. Database Not Initializing on Deployment
**Problem:** The SQLite database wasn't being created when deployed on Render, resulting in "no such table: tasks" errors.

**Solution:** Moved the `init_db()` function call outside of the `if __name__ == '__main__':` block. This ensures the database is initialized when the module loads with Gunicorn, not just when running locally with `python app.py`.

### 2. Date-Based Task Filtering
**Problem:** Needed to implement calendar-based task filtering while maintaining backward compatibility with existing tasks.

**Solution:** Added an optional `due_date` column to the database schema and used URL parameters to track and filter tasks by selected dates.

## Extra Features Added

Beyond the basic requirements, the following bonus features were implemented:

- **Calendar Date Picker:** Schedule and filter tasks by specific dates with a "Today" quick-access button
- **Dark/Light Mode:** Theme toggle with localStorage persistence and automatic system theme detection
- **Progress Tracking:** Visual progress indicators showing task completion percentage with circular charts and progress bars
- **Modern UI:** Professional design with gradient backgrounds, smooth animations, and hover effects
- **Responsive Design:** Works seamlessly on desktop and mobile devices

## Technologies Used

- **Backend:** Flask 3.0.0
- **Database:** SQLite3
- **Template Engine:** Jinja2
- **Frontend:** HTML5, CSS3, JavaScript
- **Deployment:** Render with Gunicorn
- **Version Control:** Git & GitHub



## License

This project was created as part of a Python Developer screening task.
