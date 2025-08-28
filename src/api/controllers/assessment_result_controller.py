# src/api/controllers/assessment_result_controller.py
from typing import Any, Dict, List
from flask import request, Response
from flask_restx import Namespace, Resource
from marshmallow import ValidationError
from src.api.schemas.service_schema import AssessmentResultRequestSchema, AssessmentResultResponseSchema
from src.services.assessment_result_service import AssessmentResultService
from src.infrastructure.repositories.assessment_result_repository import AssessmentResultRepository
from src.domain.exceptions import RequestNotFoundError, UserNotFoundError, ResultAlreadyExistsError
from src.api.responses import success_response, error_response

# Khởi tạo repository và service
assessment_result_repo = AssessmentResultRepository()
assessment_result_service = AssessmentResultService(assessment_result_repo)

# Namespace
api = Namespace('assessment-results', description='Assessment result operations')

assessment_result_request_schema = AssessmentResultRequestSchema()
assessment_result_response_schema_single = AssessmentResultResponseSchema()
assessment_result_response_schema_many = AssessmentResultResponseSchema(many=True)


@api.route('/')
class AssessmentResultList(Resource):
    def get(self) -> tuple[Response, int]:
        """Lấy danh sách tất cả các kết quả giám định (dành cho Admin/Manager)"""
        try:
            results = assessment_result_service.get_all_results()
            response_data: List[Dict[str, Any]] = assessment_result_response_schema_many.dump(results)  # type: ignore
            return success_response(response_data)
        except Exception as e:
            return error_response(f"Unexpected error: {str(e)}", 500)

    def post(self) -> tuple[Response, int]:
        """Tạo kết quả giám định mới"""
        try:
            json_data: Any = request.get_json()
            if not json_data:
                return error_response("Missing JSON in request.", 400)

            # Load dữ liệu và đảm bảo kiểu là dict
            raw_data = assessment_result_request_schema.load(json_data)
            if not isinstance(raw_data, dict):
                return error_response("Invalid input format.", 400)
            data: Dict[str, Any] = raw_data

            # Gọi service xử lý nghiệp vụ
            new_result = assessment_result_service.create_new_result(data)

            # Chuẩn bị response
            response_data: Dict[str, Any] = assessment_result_response_schema_single.dump(new_result)  # type: ignore
            return success_response(response_data, status_code=201)

        except ValidationError as err:
            return error_response(str(err), 400)
        except (RequestNotFoundError, UserNotFoundError) as e:
            return error_response(str(e), 404)
        except ResultAlreadyExistsError as e:
            return error_response(str(e), 409)
        except Exception as e:
            return error_response(f"Unexpected error: {str(e)}", 500)


@api.route('/<int:result_id>')
class AssessmentResult(Resource):
    def get(self, result_id: int) -> tuple[Response, int]:
        """Lấy thông tin chi tiết một kết quả giám định"""
        try:
            result = assessment_result_service.get_result_by_id(result_id)
            response_data: Dict[str, Any] = assessment_result_response_schema_single.dump(result)  # type: ignore
            return success_response(response_data)
        except RequestNotFoundError as e:
            return error_response(str(e), 404)
        except Exception as e:
            return error_response(f"Unexpected error: {str(e)}", 500)
