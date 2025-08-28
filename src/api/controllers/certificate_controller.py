# src/api/controllers/certificate_controller.py
from typing import Any, Dict, List
from flask import Response, request
from flask_restx import Namespace, Resource
from src.api.schemas.service_schema import CertificateRequestSchema, CertificateResponseSchema
from src.services.certificate_service import CertificateService
from src.infrastructure.repositories.certificate_repository import CertificateRepository
from src.domain.exceptions import CertificateAlreadyExistsError, RequestNotFoundError, ServiceNotFoundError
from src.api.responses import success_response, error_response

# Khởi tạo repository và service
certificate_repo = CertificateRepository()
certificate_service = CertificateService(certificate_repo)

api = Namespace('certificates', description='Certificate operations')

certificate_request_schema = CertificateRequestSchema()
certificate_response_schema_single = CertificateResponseSchema()
certificate_response_schema_many = CertificateResponseSchema(many=True)


@api.route('/')
class CertificateList(Resource):
    def get(self) -> tuple[Response, int]:
        """Lấy danh sách tất cả các giấy chứng nhận"""
        try:
            certificates = certificate_service.get_all_certificates()
            response_data: List[Dict[str, Any]] = certificate_response_schema_many.dump(certificates)  # type: ignore
            return success_response(response_data)
        except Exception as e:
            return error_response(str(e), 500)

    def post(self) -> tuple[Response, int]:
        """Tạo một giấy chứng nhận mới (dành cho Admin/Manager)"""
        try:
            data: Any = certificate_request_schema.load(request.json)  # type: ignore
            new_certificate = certificate_service.create_new_certificate(data)
            response_data: Dict[str, Any] = certificate_response_schema_single.dump(new_certificate)  # type: ignore
            return success_response(response_data, status_code=201)
        except RequestNotFoundError as e:
            return error_response(str(e), 404)
        except CertificateAlreadyExistsError as e:
            return error_response(str(e), 409)
        except Exception as e:
            return error_response(str(e), 400)


@api.route('/<int:certificate_id>')
class Certificate(Resource):
    def get(self, certificate_id: int) -> tuple[Response, int]:
        """Lấy thông tin chi tiết một giấy chứng nhận"""
        try:
            certificate = certificate_service.get_certificate_by_id(certificate_id)
            response_data: Dict[str, Any] = certificate_response_schema_single.dump(certificate)  # type: ignore
            return success_response(response_data)
        except RequestNotFoundError as e:
            return error_response(str(e), 404)
        except Exception as e:
            return error_response(str(e), 500)
