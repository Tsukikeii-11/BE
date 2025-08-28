# src/api/controllers/assessment_receipt_controller.py
from typing import Any, Dict, List
from flask import request, Response
from flask_restx import Namespace, Resource
from src.api.schemas.service_schema import AssessmentReceiptRequestSchema, AssessmentReceiptResponseSchema
from src.services.assessment_receipt_service import AssessmentReceiptService
from src.infrastructure.repositories.assessment_receipt_repository import AssessmentReceiptRepository
from src.domain.exceptions import RequestNotFoundError, ReceiptAlreadyExistsError, UserNotFoundError
from src.api.responses import success_response, error_response

# Khởi tạo repository và service
assessment_receipt_repo = AssessmentReceiptRepository()
assessment_receipt_service = AssessmentReceiptService(assessment_receipt_repo)

api = Namespace('assessment-receipts', description='Assessment receipt operations')

assessment_receipt_request_schema = AssessmentReceiptRequestSchema()
assessment_receipt_response_schema_single = AssessmentReceiptResponseSchema()
assessment_receipt_response_schema_many = AssessmentReceiptResponseSchema(many=True)


@api.route('/')
class AssessmentReceiptList(Resource):
    def get(self) -> tuple[Response, int]:
        """Lấy danh sách tất cả các biên nhận giám định (dành cho Admin/Manager/Consultant Staff)"""
        try:
            receipts = assessment_receipt_service.get_all_receipts()
            response_data: List[Dict[str, Any]] = assessment_receipt_response_schema_many.dump(receipts)  # type: ignore
            return success_response(response_data)
        except Exception as e:
            return error_response(f"Unexpected error: {str(e)}", 500)

    def post(self) -> tuple[Response, int]:
        """Tạo một biên nhận giám định mới (dành cho Consulting Staff)"""
        try:
            raw_data: Any = assessment_receipt_request_schema.load(request.json)  # type: ignore
            if not isinstance(raw_data, dict):
                return error_response("Invalid input format.", 400)
            data: Dict[str, Any] = raw_data

            new_receipt = assessment_receipt_service.create_new_receipt(data)
            response_data: Dict[str, Any] = assessment_receipt_response_schema_single.dump(new_receipt)  # type: ignore
            return success_response(response_data, status_code=201)
        except (RequestNotFoundError, UserNotFoundError) as e:
            return error_response(str(e), 404)
        except ReceiptAlreadyExistsError as e:
            return error_response(str(e), 409)
        except Exception as e:
            return error_response(f"Unexpected error: {str(e)}", 500)


@api.route('/<int:receipt_id>')
class AssessmentReceipt(Resource):
    def get(self, receipt_id: int) -> tuple[Response, int]:
        """Lấy thông tin chi tiết một biên nhận giám định"""
        try:
            receipt = assessment_receipt_service.get_receipt_by_id(receipt_id)
            response_data: Dict[str, Any] = assessment_receipt_response_schema_single.dump(receipt)  # type: ignore
            return success_response(response_data)
        except RequestNotFoundError as e:
            return error_response(str(e), 404)
        except Exception as e:
            return error_response(f"Unexpected error: {str(e)}", 500)
