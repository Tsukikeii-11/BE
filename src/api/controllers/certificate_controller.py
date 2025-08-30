# src/api/controllers/certificate_controller.py
from flask_restx import Namespace, Resource, fields
from api.responses import success_response, error_response

api = Namespace('certificates', description='Certificate management operations')

certificate_model = api.model('Certificate', {
    'certificate_id': fields.Integer(readonly=True, description='Certificate ID'),
    'assessment_id': fields.Integer(required=True, description='Assessment ID'),
    'certificate_code': fields.String(required=True, description='Certificate code'),
    'issue_date': fields.DateTime(readonly=True, description='Issue date'),
    'price': fields.Float(required=True, description='Certificate price'),
    'certificate_type': fields.String(required=True, description='Certificate type')
})


@api.route('/')
class CertificateList(Resource):
    @api.doc('list_certificates')
    @api.marshal_list_with(certificate_model)
    def get(self):
        """Get all certificates"""
        try:
            certificates = [
                {
                    "certificate_id": 1,
                    "assessment_id": 1,
                    "certificate_code": "CERT-2024-001",
                    "issue_date": "2024-01-24T10:00:00",
                    "price": 500000,
                    "certificate_type": "Chứng chỉ cơ bản"
                }
            ]
            return success_response({"certificates": certificates})
        except Exception as e:
            return error_response(str(e), 500)


@api.route('/<int:certificate_id>')
@api.param('certificate_id', 'The certificate identifier')
class CertificateDetail(Resource):
    @api.doc('get_certificate')
    @api.marshal_with(certificate_model)
    def get(self, certificate_id):
        """Get a certificate by ID"""
        try:
            certificate = {
                "certificate_id": certificate_id,
                "assessment_id": 1,
                "certificate_code": "CERT-2024-001",
                "issue_date": "2024-01-24T10:00:00",
                "price": 500000,
                "certificate_type": "Chứng chỉ cơ bản"
            }
            return success_response({"certificate": certificate})
        except Exception as e:
            return error_response(str(e), 404)
