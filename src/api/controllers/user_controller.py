# src/api/controllers/user_controller.py
from typing import Any
from flask import Response
from flask_restx import Namespace, Resource, fields
from src.api.responses import success_response, error_response
from src.api.schemas.user_schema import UserRegistrationSchema
from src.domain.exceptions import UserAlreadyExistsError, UserNotFoundError, InvalidDataException

# Tạo Namespace cho User
api = Namespace('users', description='User related operations')

# Swagger model
user_model = api.model('UserRegister', {
    'full_name': fields.String(required=True, description='Full name of the user'),
    'username': fields.String(required=True, description='Username of the user'),
    'password': fields.String(required=True, description='Password of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'phone_number': fields.String(required=True, description='Phone number'),
    'address': fields.String(required=False, description='Address of the user'),
    'role_name': fields.String(required=True, description='Role of the user', enum=['Admin', 'Staff', 'Manager', 'Customer'])
})

# Marshmallow schema
user_register_schema = UserRegistrationSchema()


@api.route('/register')
class UserRegister(Resource):
    @api.expect(user_model)
    def post(self) -> tuple[Response, int]:
        """Đăng ký người dùng mới"""
        try:
            data: Any = user_register_schema.load(api.payload)  # type: ignore

            # TODO: gọi service để xử lý đăng ký user
            # user = user_service.register_user(data)
            # Giả lập user đã tồn tại
            # raise UserAlreadyExistsError()

            response_data = {
                "message": "User registered successfully.",
                "user": {
                    "username": data.get('username'),
                    "email": data.get('email'),
                    "full_name": data.get('full_name'),
                    "role_name": data.get('role_name')
                }
            }
            return success_response(response_data, status_code=201)

        except UserAlreadyExistsError as e:
            return error_response(e.message, 409)
        except InvalidDataException as e:
            return error_response(e.message, 400)
        except Exception as e:
            return error_response(str(e), 500)


@api.route('/<int:user_id>')
class UserDetail(Resource):
    def get(self, user_id: int) -> tuple[Response, int]:
        """Lấy thông tin user theo ID"""
        try:
            # TODO: gọi service lấy user
            # user = user_service.get_user_by_id(user_id)
            # Giả lập user không tồn tại
            # raise UserNotFoundError(user_id)

            response_data = {
                "message": "User found.",
                "user": {
                    "user_id": user_id,
                    "full_name": "Nguyen Van A",
                    "username": "nguyenvana",
                    "email": "nguyenvana@example.com",
                    "role_name": "Customer",
                    "phone_number": "0909123456",
                    "address": "123 Ho Chi Minh Street"
                }
            }
            return success_response(response_data)

        except UserNotFoundError as e:
            return error_response(e.message, 404)
        except Exception as e:
            return error_response(str(e), 500)
