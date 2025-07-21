from flask import Blueprint, request, jsonify
from src.services.todo_service import TodoService
from src.infrastructure.repositories.todo_repository import TodoRepository
from src.api.schemas.todo import TodoRequestSchema, TodoResponseSchema
from datetime import datetime

bp = Blueprint('todo', __name__, url_prefix='/todos')

# Khởi tạo service và repository (dùng memory, chưa kết nối DB thật)
todo_service = TodoService(TodoRepository())

request_schema = TodoRequestSchema()
response_schema = TodoResponseSchema()

@bp.route('/', methods=['GET'])
def list_todos():
    todos = todo_service.list_todos()
    return jsonify(response_schema.dump(todos, many=True)), 200

@bp.route('/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = todo_service.get_todo(todo_id)
    if not todo:
        return jsonify({'message': 'Todo not found'}), 404
    return jsonify(response_schema.dump(todo)), 200

@bp.route('/', methods=['POST'])
def create_todo():
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    now = datetime.utcnow()
    todo = todo_service.create_todo(
        title=data['title'],
        description=data['description'],
        status=data['status'],
        created_at=now,
        updated_at=now
    )
    return jsonify(response_schema.dump(todo)), 201

@bp.route('/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    todo = todo_service.update_todo(
        todo_id=todo_id,
        title=data['title'],
        description=data['description'],
        status=data['status'],
        created_at=datetime.utcnow(),  # Có thể lấy từ DB nếu cần
        updated_at=datetime.utcnow()
    )
    return jsonify(response_schema.dump(todo)), 200

@bp.route('/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo_service.delete_todo(todo_id)
    return '', 204 