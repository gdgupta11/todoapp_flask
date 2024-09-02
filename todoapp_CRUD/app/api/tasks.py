from flask import jsonify, request
from app import db
from app.models.tasks import Task
from app.api import bp

@bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify(tasks=[task.to_dict() for task in tasks]), 200

@bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json() or {}
    task = Task.query.get_or_404(id)
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.complete = data.get('complete', task.complete)
    db.session.commit()
    return jsonify(task.to_dict()), 200

@bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return '', 204

# write a function to get the task by id using rest api
@bp.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify(task.to_dict()), 200