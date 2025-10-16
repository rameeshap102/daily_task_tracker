from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import sqlite3
import os


app = Flask(__name__)


# Database initialization with due_date column added
def init_db():
    if os.path.exists('tasks.db'):
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        try:
            cursor.execute("PRAGMA table_info(tasks)")
            columns = [col[1] for col in cursor.fetchall()]
            if 'completed' not in columns or 'due_date' not in columns:
                cursor.execute('DROP TABLE IF EXISTS tasks')
                conn.commit()
        except:
            pass
        conn.close()
    
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  created_at TEXT NOT NULL,
                  due_date TEXT,
                  completed INTEGER DEFAULT 0,
                  completed_at TEXT)''')
    conn.commit()
    conn.close()


def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    # Get selected date from URL parameter, default to today
    selected_date = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))
    
    conn = get_db_connection()
    # Filter tasks by selected date or show all if no date specified
    tasks_raw = conn.execute('SELECT * FROM tasks WHERE due_date = ? ORDER BY created_at DESC', (selected_date,)).fetchall()
    conn.close()
    
    tasks_list = []
    for task in tasks_raw:
        task_dict = {
            'id': task['id'],
            'title': task['title'],
            'created_at': task['created_at'],
            'due_date': task['due_date'] if 'due_date' in task.keys() else None,
            'completed': task['completed'],
            'completed_at': task['completed_at'] if 'completed_at' in task.keys() else None
        }
        tasks_list.append(task_dict)
    
    total_tasks = len(tasks_list)
    completed_tasks = sum(1 for task in tasks_list if task['completed'] == 1)
    pending_tasks = total_tasks - completed_tasks
    progress = int((completed_tasks / total_tasks * 100)) if total_tasks > 0 else 0
    
    today_date = datetime.now().strftime('%A, %B %d, %Y')
    
    return render_template('index.html', 
                         tasks=tasks_list, 
                         total_tasks=total_tasks,
                         completed_tasks=completed_tasks,
                         pending_tasks=pending_tasks,
                         progress=progress,
                         today_date=today_date,
                         selected_date=selected_date)


@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    due_date = request.form.get('due_date')
    
    if title:
        conn = get_db_connection()
        created_at = datetime.now().strftime('%Y-%m-%d %I:%M %p')
        
        # If no due_date provided, use today's date
        if not due_date:
            due_date = datetime.now().strftime('%Y-%m-%d')
        
        conn.execute('INSERT INTO tasks (title, created_at, due_date, completed) VALUES (?, ?, ?, ?)',
                    (title, created_at, due_date, 0))
        conn.commit()
        conn.close()
    
    # Redirect back to the selected date
    redirect_date = due_date if due_date else datetime.now().strftime('%Y-%m-%d')
    return redirect(url_for('index', date=redirect_date))


@app.route('/edit/<int:task_id>', methods=['GET'])
def edit_task_page(task_id):
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    conn.close()
    
    if task is None:
        return redirect(url_for('index'))
    
    task_dict = {
        'id': task['id'],
        'title': task['title'],
        'created_at': task['created_at'],
        'due_date': task['due_date'] if 'due_date' in task.keys() else None,
        'completed': task['completed'],
        'completed_at': task['completed_at'] if 'completed_at' in task.keys() else None
    }
    
    return render_template('edit.html', task=task_dict)


@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    title = request.form.get('title')
    due_date = request.form.get('due_date')
    
    if title:
        conn = get_db_connection()
        if due_date:
            conn.execute('UPDATE tasks SET title = ?, due_date = ? WHERE id = ?', (title, due_date, task_id))
        else:
            conn.execute('UPDATE tasks SET title = ? WHERE id = ?', (title, task_id))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))


@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    selected_date = request.form.get('date', datetime.now().strftime('%Y-%m-%d'))
    conn = get_db_connection()
    completed_at = datetime.now().strftime('%Y-%m-%d %I:%M %p')
    conn.execute('UPDATE tasks SET completed = 1, completed_at = ? WHERE id = ?',
                (completed_at, task_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index', date=selected_date))


@app.route('/uncomplete/<int:task_id>', methods=['POST'])
def uncomplete_task(task_id):
    selected_date = request.form.get('date', datetime.now().strftime('%Y-%m-%d'))
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET completed = 0, completed_at = NULL WHERE id = ?',
                (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index', date=selected_date))


@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    selected_date = request.form.get('date', datetime.now().strftime('%Y-%m-%d'))
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index', date=selected_date))


@app.route('/clear_completed', methods=['POST'])
def clear_completed():
    selected_date = request.form.get('date', datetime.now().strftime('%Y-%m-%d'))
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE completed = 1 AND due_date = ?', (selected_date,))
    conn.commit()
    conn.close()
    return redirect(url_for('index', date=selected_date))


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
