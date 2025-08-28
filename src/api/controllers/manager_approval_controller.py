# src/api/controllers/manager_approval_controller.py
from typing import Any, Dict, List
from flask import Response, request
from flask_restx import Namespace, Resource
from src.api.schemas.service_schema import ManagerApprovalRequestSchema, ManagerApprovalResponseSchema
from src.services.manager_approval_service import ManagerApprovalService
from src.infrastructure.repositories.manager_approval_repository import ManagerApprovalRepository
from src.domain.exceptions import RequestNotFoundError, ApprovalAlreadyExistsError, UserNotFoundError
from src.api.responses import success_response, error_response

# Khởi tạo repository và service
manager_approval_repo = ManagerApprovalRepository()
manager_approval_service = ManagerApprovalService(manager_approval_repo)

api = Namespace('manager-approvals', description='Manager approval operations')

manager_approval_request_schema = ManagerApprovalRequestSchema()
manager_approval_response_schema_single = ManagerApprovalResponseSchema()
manager_approval_response_schema_many = ManagerApprovalResponseSchema(many=True)


@api.route('/')
class ManagerApprovalList(Resource):
    def get(self) -> tuple[Response, int]:
        """Lấy danh sách tất cả các phê duyệt của quản lý (dành cho Admin)"""
        try:
            approvals = manager_approval_service.get_all_approvals()
            response_data: List[Dict[str, Any]] = manager_approval_response_schema_many.dump(approvals)  # type: ignore
            return success_response(response_data)
        except Exception as e:
            return error_response(str(e), 500)

    def post(self) -> tuple[Response, int]:
        """Tạo một phê duyệt mới (dành cho Manager)"""
        try:
            data: Any = manager_approval_request_schema.load(request.json)  # type: ignore
            new_approval = manager_approval_service.create_new_approval(data)
            response_data: Dict[str, Any] = manager_approval_response_schema_single.dump(new_approval)  # type: ignore
            return success_response(response_data, status_code=201)
        except (RequestNotFoundError, UserNotFoundError) as e:
            return error_response(str(e), 404)
        except ApprovalAlreadyExistsError as e:
            return error_response(str(e), 409)
        except Exception as e:
            return error_response(str(e), 400)


@api.route('/<int:approval_id>')
class ManagerApproval(Resource):
    def get(self, approval_id: int) -> tuple[Response, int]:
        """Lấy thông tin chi tiết một phê duyệt của quản lý"""
        try:
            approval = manager_approval_service.get_approval_by_id(approval_id)
            response_data: Dict[str, Any] = manager_approval_response_schema_single.dump(approval)  # type: ignore
            return success_response(response_data)
        except RequestNotFoundError as e:
            return error_response(str(e), 404)
        except Exception as e:
            return error_response(str(e), 500)
