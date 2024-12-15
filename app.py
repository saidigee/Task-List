import os
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory task storage (would be a database in a real application)
tasks = []

@app.route('/', methods=['GET', 'POST'])
def task_list():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        
        # Create new task
        task = {
            'id': len(tasks) + 1,
            'title': title,
            'description': description,
            'created_at': datetime.now(),
            'completed': False
        }
        tasks.append(task)
        return redirect(url_for('task_list'))
    
    return render_template('tasks.html', tasks=tasks)

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            break
    return redirect(url_for('task_list'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('task_list'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))