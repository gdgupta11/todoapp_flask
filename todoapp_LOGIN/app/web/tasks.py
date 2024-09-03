from flask import render_template, request, redirect, url_for, flash, current_app
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.models.tasks import Task
from app.models.users import User
from app.web import bp
from werkzeug.security import generate_password_hash, check_password_hash

@bp.route('/')
@login_required
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks, task="TASK WEBPAGE")

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('web.index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            flash('Invalid username or password')
            return redirect(url_for('web.login'))
        login_user(user)
        return redirect(url_for('web.index'))
    return render_template('login.html')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.login'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        current_app.logger.info(f"User {current_user.username} is already authenticated")
        return redirect(url_for('web.index'))
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user is not None:
            flash('Username already exists')
            current_app.logger.info(f"Username {username} already exists")
            return redirect(url_for('web.register'))
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful')
        current_app.logger.info(f"User {username} registered successfully")
        return redirect(url_for('web.login'))
    return render_template('register.html')

@bp.route('/create', methods=['POST'])
@login_required
def create():
    title = request.form['task']
    description = request.form['description']
    complete = request.form.get('complete', False)
    
    try:
        new_task = Task(title=title, description=description, complete=complete)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully')
        current_app.logger.info(f'New task added successfully')
    except Exception as e:
        db.session.rollback()
        flash(f'Error adding task: {str(e)}')
        current_app.logger.error(f'Error adding task: {str(e)}')
    
    return redirect(url_for('web.index'))

@bp.route('/update/<int:id>', methods=['POST'])
@login_required
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
@login_required
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


@bp.route('/get/<int:id>', methods=['GET'])
@login_required
def get(id):
    task = Task.query.get_or_404(id)
    current_app.logger.info(f"Task {id} retrieved successfully")
    return render_template('task.html', task=task)

