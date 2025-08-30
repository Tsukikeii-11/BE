# src/api/controllers/user_controller.py
from typing import Any
from flask import Response
from flask_restx import Namespace, Resource, fields
from api.responses import success_response, error_response
from api.schemas.user_schema import UserRegistrationSchema
from domain.exceptions import UserAlreadyExistsError, UserNotFoundError, InvalidDataException

# Tạo Namespace cho User
api = Namespace('users', description='User management operations')

# Swagger models
user_model = api.model('User', {
    'user_id': fields.Integer(readonly=True, description='User ID'),
    'username': fields.String(required=True, description='Username of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'full_name': fields.String(required=True, description='Full name of the user'),
    'phone_number': fields.String(required=True, description='Phone number'),
    'address': fields.String(required=False, description='Address of the user'),
    'role_name': fields.String(required=True, description='Role of the user', enum=['Admin', 'Manager', 'Consulting Staff', 'Assessment Staff', 'Customer'])
})

user_create_model = api.model('UserCreate', {
    'username': fields.String(required=True, description='Username of the user'),
    'password': fields.String(required=True, description='Password of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'full_name': fields.String(required=True, description='Full name of the user'),
    'phone_number': fields.String(required=True, description='Phone number'),
    'address': fields.String(required=False, description='Address of the user'),
    'role_name': fields.String(required=True, description='Role of the user', enum=['Admin', 'Manager', 'Consulting Staff', 'Assessment Staff', 'Customer'])
})

user_update_model = api.model('UserUpdate', {
    'full_name': fields.String(required=False, description='Full name of the user'),
    'email': fields.String(required=False, description='Email of the user'),
    'phone_number': fields.String(required=False, description='Phone number'),
    'address': fields.String(required=False, description='Address of the user'),
    'role_name': fields.String(required=False, description='Role of the user', enum=['Admin', 'Manager', 'Consulting Staff', 'Assessment Staff', 'Customer'])
})

# Marshmallow schema
user_register_schema = UserRegistrationSchema()


@api.route('/')
class UserList(Resource):
    @api.doc('list_users')
    @api.marshal_list_with(user_model)
    def get(self):
        """Get all users"""
        try:
            # Mock data for demonstration
            users = [
                {
                    "user_id": 1,
                    "username": "admin",
                    "email": "admin@diamond.com",
                    "full_name": "Nguyen Van Admin",
                    "phone_number": "0901234567",
                    "address": "123 Duong ABC, Quan 1, TP.HCM",
                    "role_name": "Admin"
                },
                {
                    "user_id": 2,
                    "username": "manager",
                    "email": "manager@diamond.com",
                    "full_name": "Tran Thi Manager",
                    "phone_number": "0901234568",
                    "address": "456 Duong XYZ, Quan 3, TP.HCM",
                    "role_name": "Manager"
                }
            ]
            return success_response({"users": users})
        except Exception as e:
            return error_response(str(e), 500)

    @api.doc('create_user')
    @api.expect(user_create_model)
    @api.marshal_with(user_model)
    @api.response(201, 'User created successfully')
    def post(self):
        """Create a new user"""
        try:
            data = api.payload
            # TODO: Validate data and call service
            response_data = {
                "message": "User created successfully.",
                "user": {
                    "user_id": 3,
                    "username": data.get('username'),
                    "email": data.get('email'),
                    "full_name": data.get('full_name'),
                    "phone_number": data.get('phone_number'),
                    "address": data.get('address'),
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
@api.param('user_id', 'The user identifier')
class UserDetail(Resource):
    @api.doc('get_user')
    @api.marshal_with(user_model)
    def get(self, user_id):
        """Get a user by ID"""
        try:
            # Mock data for demonstration
            user = {
                "user_id": user_id,
                "username": "nguyenvana",
                "email": "nguyenvana@example.com",
                "full_name": "Nguyen Van A",
                "phone_number": "0909123456",
                "address": "123 Ho Chi Minh Street",
                "role_name": "Customer"
            }
            return success_response({"user": user})
        except UserNotFoundError as e:
            return error_response(e.message, 404)
        except Exception as e:
            return error_response(str(e), 500)

    @api.doc('update_user')
    @api.expect(user_update_model)
    @api.marshal_with(user_model)
    def put(self, user_id):
        """Update a user completely"""
        try:
            data = api.payload
            # TODO: Update user logic
            response_data = {
                "message": "User updated successfully.",
                "user": {
                    "user_id": user_id,
                    "username": "nguyenvana",
                    "email": data.get('email', "nguyenvana@example.com"),
                    "full_name": data.get('full_name', "Nguyen Van A"),
                    "phone_number": data.get('phone_number', "0909123456"),
                    "address": data.get('address', "123 Ho Chi Minh Street"),
                    "role_name": data.get('role_name', "Customer")
                }
            }
            return success_response(response_data)
        except UserNotFoundError as e:
            return error_response(e.message, 404)
        except Exception as e:
            return error_response(str(e), 500)

    @api.doc('update_user_partial')
    @api.expect(user_update_model)
    @api.marshal_with(user_model)
    def patch(self, user_id):
        """Update a user partially"""
        try:
            data = api.payload
            # TODO: Partial update logic
            response_data = {
                "message": "User updated successfully.",
                "user": {
                    "user_id": user_id,
                    "username": "nguyenvana",
                    "email": data.get('email', "nguyenvana@example.com"),
                    "full_name": data.get('full_name', "Nguyen Van A"),
                    "phone_number": data.get('phone_number', "0909123456"),
                    "address": data.get('address', "123 Ho Chi Minh Street"),
                    "role_name": data.get('role_name', "Customer")
                }
            }
            return success_response(response_data)
        except UserNotFoundError as e:
            return error_response(e.message, 404)
        except Exception as e:
            return error_response(str(e), 500)

    @api.doc('delete_user')
    def delete(self, user_id):
        """Delete a user"""
        try:
            # TODO: Delete user logic
            return success_response({"message": f"User {user_id} deleted successfully."})
        except UserNotFoundError as e:
            return error_response(e.message, 404)
        except Exception as e:
            return error_response(str(e), 500)
