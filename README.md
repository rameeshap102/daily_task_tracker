# Daily Task Tracker

A Flask-based web application for managing daily tasks with a beautiful, modern interface.

## Live Demo

**Hosted App:** https://daily-task-tracker-o6ty.onrender.com/

**GitHub Repository:** https://github.com/rameeshap102/daily_task_tracker

## Features

### Core Features
- Add new tasks with title and date selection
- Edit existing tasks to update details
- Delete individual tasks with confirmation
- Mark tasks as completed/incomplete with one click
- View all tasks organized by date
- Clear all completed tasks at once
- Persistent data storage with SQLite database

### Advanced Features
- **Calendar Date Picker:** Interactive calendar for selecting task due dates with "Today" quick-access button
- **Date-Based Filtering:** View and manage tasks for specific dates
- **Dark/Light Mode:** Manual theme toggle with automatic system preference detection and localStorage persistence
- **Progress Dashboard:** Real-time statistics showing total, pending, and completed task counts
- **Visual Progress Indicators:** 
  - Circular progress chart showing completion percentage
  - Progress bars for each task category
  - Color-coded gradient stat cards (Blue, Purple, Green, Orange)
- **Smooth Animations:** Fade-in effects, hover states, and transitions throughout
- **Responsive Design:** Mobile-optimized interface that works perfectly on all screen sizes
- **Keyboard Support:** Press Escape to clear input fields, Enter to add tasks
- **Professional UI:** Modern design with gradient backgrounds and glass morphism effects
- **Task Organization:** Separate sections for pending and completed tasks with badges
- **Action Buttons:** Edit and delete buttons appear on hover for clean interface
- **Auto-sorting:** Tasks automatically sorted by creation date

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
- Auto-deployment: Enabled via GitHub integration

## Difficulties Faced

### 1. Database Not Initializing on Deployment
**Problem:** The SQLite database wasn't being created when deployed on Render, resulting in "no such table: tasks" errors.

**Solution:** Moved the `init_db()` function call outside of the `if __name__ == '__main__':` block. This ensures the database is initialized when the module loads with Gunicorn, not just when running locally with `python app.py`.

### 2. Date-Based Task Filtering
**Problem:** Needed to implement calendar-based task filtering while maintaining backward compatibility with existing tasks.

**Solution:** Added an optional `due_date` column to the database schema and used URL parameters to track and filter tasks by selected dates.

### 3. Mobile Responsiveness for Stats Cards
**Problem:** Progress ring and stat cards were overflowing on mobile screens, breaking the layout.

**Solution:** Implemented CSS media queries with responsive grid layouts - 4 columns on desktop, 2 on tablets, 1 on mobile. Adjusted SVG dimensions and font sizes for optimal mobile viewing.

## Technologies Used

- **Backend:** Flask 3.0.0
- **Database:** SQLite3
- **Template Engine:** Jinja2
- **Frontend:** HTML5, CSS3 (with CSS Grid & Flexbox), JavaScript (ES6+)
- **Deployment:** Render with Gunicorn 21.2.0
- **Version Control:** Git & GitHub


## Design Highlights

- **Color Scheme:** Blue gradients for primary actions, green for completed, orange for pending
- **Typography:** Segoe UI font family for clean, modern look
- **Animations:** Smooth fade-in, slide-in, and hover transitions
- **Dark Mode:** Full dark theme with adjusted colors and contrasts
- **Accessibility:** Clear visual feedback, proper contrast ratios, keyboard navigation

## Future Enhancements

- Task categories/tags
- Priority levels
- Due time (not just date)
- Recurring tasks
- Search and filter functionality
- Export tasks to CSV
- User authentication
- Task reminders/notifications

## License

This project was created as part of a Python Developer screening task.

---

**⭐ Live Demo:** https://daily-task-tracker-o6ty.onrender.com/

