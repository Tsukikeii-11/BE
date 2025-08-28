# src/api/controllers/service_controller.py
from typing import Any, Dict, List
from flask import Response, request
from flask_restx import Namespace, Resource
from src.api.schemas.service_schema import ServiceRequestSchema, ServiceResponseSchema
from src.services.service_service import ServiceService
from src.infrastructure.repositories.service_repository import ServiceRepository
from src.domain.exceptions import ServiceNameConflictError
from src.api.responses import success_response, error_response

# Khởi tạo repository và service
service_repo = ServiceRepository()
service_service = ServiceService(service_repo)

api = Namespace('services', description='Services related operations')

service_request_schema = ServiceRequestSchema()
service_response_schema_many = ServiceResponseSchema(many=True)
service_response_schema_single = ServiceResponseSchema()


@api.route('/')
class ServiceList(Resource):
    def get(self) -> tuple[Response, int]:
        """Lấy danh sách tất cả các dịch vụ"""
        try:
            services = service_service.get_all_services()
            response_data: List[Dict[str, Any]] = service_response_schema_many.dump(services)  # type: ignore
            return success_response(response_data)
        except Exception as e:
            return error_response(str(e), 500)

    def post(self) -> tuple[Response, int]:
        """Tạo một dịch vụ mới"""
        try:
            data: Any = service_request_schema.load(request.json)  # type: ignore
            new_service = service_service.create_new_service(data)
            response_data: Dict[str, Any] = service_response_schema_single.dump(new_service)  # type: ignore
            return success_response(response_data, status_code=201)
        except ServiceNameConflictError as e:
            return error_response(str(e), 409)
        except Exception as e:
            return error_response(str(e), 400)
