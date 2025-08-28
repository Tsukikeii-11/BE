# src/api/controllers/assessment_request_controller.py
from typing import Any, Dict, List
from flask import Response, request
from flask_restx import Namespace, Resource
from src.api.schemas.service_schema import AssessmentRequestSchema, AssessmentRequestResponseSchema
from src.services.assessment_request_service import AssessmentRequestService
from src.infrastructure.repositories.assessment_request_repository import AssessmentRequestRepository
from src.domain.exceptions import RequestNotFoundError, UserNotFoundError, ServiceNotFoundError
from src.api.responses import success_response, error_response

# Khởi tạo repository và service
assessment_request_repo = AssessmentRequestRepository()
assessment_request_service = AssessmentRequestService(assessment_request_repo)

api = Namespace('assessment-requests', description='Assessment request operations')

assessment_request_schema = AssessmentRequestSchema()
assessment_request_response_schema_single = AssessmentRequestResponseSchema()
assessment_request_response_schema_many = AssessmentRequestResponseSchema(many=True)


@api.route('/')
class AssessmentRequestList(Resource):
    def get(self) -> tuple[Response, int]:
        """Lấy danh sách tất cả các yêu cầu giám định"""
        try:
            requests = assessment_request_service.get_all_requests()
            response_data: List[Dict[str, Any]] = assessment_request_response_schema_many.dump(requests)  # type: ignore
            return success_response(response_data)
        except Exception as e:
            return error_response(str(e), 500)

    def post(self) -> tuple[Response, int]:
        """Tạo một yêu cầu giám định mới"""
        try:
            data: Any = assessment_request_schema.load(request.json)  # type: ignore
            new_request = assessment_request_service.create_new_request(data)
            response_data: Dict[str, Any] = assessment_request_response_schema_single.dump(new_request)  # type: ignore
            return success_response(response_data, status_code=201)
        except (UserNotFoundError, ServiceNotFoundError) as e:
            return error_response(str(e), 404)
        except Exception as e:
            return error_response(str(e), 400)


@api.route('/<int:request_id>')
class AssessmentRequest(Resource):
    def get(self, request_id: int) -> tuple[Response, int]:
        """Lấy thông tin chi tiết một yêu cầu giám định"""
        try:
            request_item = assessment_request_service.get_request_by_id(request_id)
            response_data: Dict[str, Any] = assessment_request_response_schema_single.dump(request_item)  # type: ignore
            return success_response(response_data)
        except RequestNotFoundError as e:
            return error_response(str(e), 404)
        except Exception as e:
            return error_response(str(e), 500)
