from flask import jsonify, request, current_app
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app import db
from app.models.tasks import Task
from app.models.users import User
from app.api import bp
from werkzeug.security import check_password_hash

# Initialize Limiter
limiter = Limiter(key_func=get_remote_address, default_limits=["60 per minute"])

@bp.route('/login', methods=['POST'])
@limiter.limit("10 per minute")  # Limit login attempts
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        current_app.logger.error(f"Invalid login attempt for user: {username}")
        return jsonify({"msg": "Invalid username or password"}), 401
    access_token = create_access_token(identity=user.id)
    current_app.logger.info(f"User {username} logged in successfully")
    return jsonify(access_token=access_token), 200

@bp.route('/tasks', methods=['GET'])
@jwt_required()
@limiter.limit("60 per minute")
def get_tasks():
    current_user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=current_user_id).all()
    current_app.logger.info(f"Tasks retrieved for user {current_user_id}")
    return jsonify(tasks=[task.to_dict() for task in tasks]), 200

@bp.route('/tasks/<int:id>', methods=['PUT'])
@jwt_required()
@limiter.limit("60 per minute")
def update_task(id):
    current_user_id = get_jwt_identity()
    task = Task.query.filter_by(id=id, user_id=current_user_id).first_or_404()
    data = request.get_json() or {}
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.complete = data.get('complete', task.complete)
    db.session.commit()
    current_app.logger.info(f"Task {id} updated successfully")
    return jsonify(task.to_dict()), 200

@bp.route('/tasks/<int:id>', methods=['DELETE'])
@jwt_required()
@limiter.limit("60 per minute")
def delete_task(id):
    current_user_id = get_jwt_identity()
    task = Task.query.filter_by(id=id, user_id=current_user_id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    current_app.logger.info(f"Task {id} deleted successfully")
    return '', 204

@bp.route('/tasks/<int:id>', methods=['GET'])
@jwt_required()
@limiter.limit("60 per minute")
def get_task(id):
    current_user_id = get_jwt_identity()
    task = Task.query.filter_by(id=id, user_id=current_user_id).first_or_404()
    current_app.logger.info(f"Task {id} retrieved successfully")
    return jsonify(task.to_dict()), 200