# src/api/controllers/service_controller.py
from typing import Any, Dict, List
from flask import Response, request
from flask_restx import Namespace, Resource, fields
from api.schemas.service_schema import ServiceRequestSchema, ServiceResponseSchema
from services.service_service import ServiceService
from infrastructure.repositories.service_repository import ServiceRepository
from domain.exceptions import ServiceNameConflictError
from api.responses import success_response, error_response

# Khởi tạo repository và service
service_repo = ServiceRepository()
service_service = ServiceService(service_repo)

api = Namespace('services', description='Diamond assessment services management')

# Swagger models
service_model = api.model('Service', {
    'service_id': fields.Integer(readonly=True, description='Service ID'),
    'service_name': fields.String(required=True, description='Name of the service'),
    'description': fields.String(required=False, description='Service description'),
    'price': fields.Float(required=True, description='Service price'),
    'estimated_duration_days': fields.Integer(required=True, description='Estimated duration in days'),
    'is_active': fields.Boolean(required=False, description='Service status')
})

service_create_model = api.model('ServiceCreate', {
    'service_name': fields.String(required=True, description='Name of the service'),
    'description': fields.String(required=False, description='Service description'),
    'price': fields.Float(required=True, description='Service price'),
    'estimated_duration_days': fields.Integer(required=True, description='Estimated duration in days')
})

service_update_model = api.model('ServiceUpdate', {
    'service_name': fields.String(required=False, description='Name of the service'),
    'description': fields.String(required=False, description='Service description'),
    'price': fields.Float(required=False, description='Service price'),
    'estimated_duration_days': fields.Integer(required=False, description='Estimated duration in days'),
    'is_active': fields.Boolean(required=False, description='Service status')
})

service_request_schema = ServiceRequestSchema()
service_response_schema_many = ServiceResponseSchema(many=True)
service_response_schema_single = ServiceResponseSchema()


@api.route('/')
class ServiceList(Resource):
    @api.doc('list_services')
    @api.marshal_list_with(service_model)
    def get(self):
        """Get all services"""
        try:
            # Mock data for demonstration
            services = [
                {
                    "service_id": 1,
                    "service_name": "Giám định kim cương cơ bản",
                    "description": "Giám định các thông số cơ bản của kim cương",
                    "price": 500000,
                    "estimated_duration_days": 3,
                    "is_active": True
                },
                {
                    "service_id": 2,
                    "service_name": "Giám định kim cương nâng cao",
                    "description": "Giám định chi tiết với báo cáo đầy đủ",
                    "price": 800000,
                    "estimated_duration_days": 5,
                    "is_active": True
                },
                {
                    "service_id": 3,
                    "service_name": "Giám định kim cương cao cấp",
                    "description": "Giám định với chứng chỉ quốc tế",
                    "price": 1200000,
                    "estimated_duration_days": 7,
                    "is_active": True
                }
            ]
            return success_response({"services": services})
        except Exception as e:
            return error_response(str(e), 500)

    @api.doc('create_service')
    @api.expect(service_create_model)
    @api.marshal_with(service_model)
    @api.response(201, 'Service created successfully')
    def post(self):
        """Create a new service"""
        try:
            data = api.payload
            # TODO: Validate data and call service
            response_data = {
                "message": "Service created successfully.",
                "service": {
                    "service_id": 4,
                    "service_name": data.get('service_name'),
                    "description": data.get('description'),
                    "price": data.get('price'),
                    "estimated_duration_days": data.get('estimated_duration_days'),
                    "is_active": True
                }
            }
            return success_response(response_data, status_code=201)
        except ServiceNameConflictError as e:
            return error_response(str(e), 409)
        except Exception as e:
            return error_response(str(e), 400)


@api.route('/<int:service_id>')
@api.param('service_id', 'The service identifier')
class ServiceDetail(Resource):
    @api.doc('get_service')
    @api.marshal_with(service_model)
    def get(self, service_id):
        """Get a service by ID"""
        try:
            # Mock data for demonstration
            service = {
                "service_id": service_id,
                "service_name": "Giám định kim cương cơ bản",
                "description": "Giám định các thông số cơ bản của kim cương",
                "price": 500000,
                "estimated_duration_days": 3,
                "is_active": True
            }
            return success_response({"service": service})
        except Exception as e:
            return error_response(str(e), 404)

    @api.doc('update_service')
    @api.expect(service_update_model)
    @api.marshal_with(service_model)
    def put(self, service_id):
        """Update a service completely"""
        try:
            data = api.payload
            # TODO: Update service logic
            response_data = {
                "message": "Service updated successfully.",
                "service": {
                    "service_id": service_id,
                    "service_name": data.get('service_name', "Giám định kim cương cơ bản"),
                    "description": data.get('description', "Giám định các thông số cơ bản của kim cương"),
                    "price": data.get('price', 500000),
                    "estimated_duration_days": data.get('estimated_duration_days', 3),
                    "is_active": data.get('is_active', True)
                }
            }
            return success_response(response_data)
        except Exception as e:
            return error_response(str(e), 404)

    @api.doc('update_service_partial')
    @api.expect(service_update_model)
    @api.marshal_with(service_model)
    def patch(self, service_id):
        """Update a service partially"""
        try:
            data = api.payload
            # TODO: Partial update logic
            response_data = {
                "message": "Service updated successfully.",
                "service": {
                    "service_id": service_id,
                    "service_name": data.get('service_name', "Giám định kim cương cơ bản"),
                    "description": data.get('description', "Giám định các thông số cơ bản của kim cương"),
                    "price": data.get('price', 500000),
                    "estimated_duration_days": data.get('estimated_duration_days', 3),
                    "is_active": data.get('is_active', True)
                }
            }
            return success_response(response_data)
        except Exception as e:
            return error_response(str(e), 404)

    @api.doc('delete_service')
    def delete(self, service_id):
        """Delete a service"""
        try:
            # TODO: Delete service logic
            return success_response({"message": f"Service {service_id} deleted successfully."})
        except Exception as e:
            return error_response(str(e), 404)
