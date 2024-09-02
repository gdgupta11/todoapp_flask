from flask import render_template, request, redirect, url_for, flash, current_app
from app import db
from app.models.tasks import Task
from app.web import bp

@bp.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks, task="TASK WEBPAGE")

@bp.route('/create', methods=['POST'])
def create():
    title = request.form['task']
    description = request.form['description']
    complete = request.form.get('complete', False)
    
    try:
        new_task = Task(title=title, description=description, complete=complete)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully')
        current_app.logger.info('New task added successfully')
    except Exception as e:
        db.session.rollback()
        flash(f'Error adding task: {str(e)}')
        current_app.logger.error(f'Error adding task: {str(e)}')
    
    return redirect(url_for('web.index'))

@bp.route('/update/<int:id>', methods=['POST'])
def update(id):
    task = Task.query.get_or_404(id)
    task.title = request.form['task']
    task.description = request.form['description']
    task.complete = 'complete' in request.form
    
    try:
        db.session.commit()
        flash('Task updated successfully')
        current_app.logger.info(f'Task {id} updated successfully')
    except Exception as e:
        db.session.rollback()
        flash(f'Error updating task: {str(e)}')
        current_app.logger.error(f'Error updating task {id}: {str(e)}')
    
    return redirect(url_for('web.index'))

@bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    task = Task.query.get_or_404(id)
    
    try:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted successfully')
        current_app.logger.info(f'Task {id} deleted successfully')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting task: {str(e)}')
        current_app.logger.error(f'Error deleting task {id}: {str(e)}')
    
    return redirect(url_for('web.index'))

# write a function to get the task by id
@bp.route('/get/<int:id>', methods=['GET'])
def get(id):
    task = Task.query.get_or_404(id)
    return render_template('task.html', task=task)

