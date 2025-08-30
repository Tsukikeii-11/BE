# src/api/controllers/assessment_receipt_controller.py
from flask_restx import Namespace, Resource, fields
from api.responses import success_response, error_response

api = Namespace('receipts', description='Assessment receipt management operations')

receipt_model = api.model('AssessmentReceipt', {
    'receipt_id': fields.Integer(readonly=True, description='Receipt ID'),
    'request_id': fields.Integer(required=True, description='Request ID'),
    'consultant_staff_id': fields.Integer(required=True, description='Consultant staff ID'),
    'receive_date': fields.DateTime(readonly=True, description='Receive date'),
    'sample_description': fields.String(required=True, description='Sample description'),
    'sample_condition': fields.String(required=True, description='Sample condition')
})

receipt_create_model = api.model('AssessmentReceiptCreate', {
    'request_id': fields.Integer(required=True, description='Request ID'),
    'consultant_staff_id': fields.Integer(required=True, description='Consultant staff ID'),
    'sample_description': fields.String(required=True, description='Sample description'),
    'sample_condition': fields.String(required=True, description='Sample condition')
})


@api.route('/')
class AssessmentReceiptList(Resource):
    @api.doc('list_receipts')
    @api.marshal_list_with(receipt_model)
    def get(self):
        """Get all assessment receipts"""
        try:
            receipts = [
                {
                    "receipt_id": 1,
                    "request_id": 1,
                    "consultant_staff_id": 3,
                    "receive_date": "2024-01-21T09:00:00",
                    "sample_description": "Kim cương tròn 1.5 carat, màu D, độ tinh khiết VVS1",
                    "sample_condition": "Tốt"
                }
            ]
            return success_response({"receipts": receipts})
        except Exception as e:
            return error_response(str(e), 500)

    @api.doc('create_receipt')
    @api.expect(receipt_create_model)
    @api.marshal_with(receipt_model)
    @api.response(201, 'Assessment receipt created successfully')
    def post(self):
        """Create a new assessment receipt"""
        try:
            data = api.payload
            response_data = {
                "message": "Assessment receipt created successfully.",
                "receipt": {
                    "receipt_id": 2,
                    "request_id": data.get('request_id'),
                    "consultant_staff_id": data.get('consultant_staff_id'),
                    "receive_date": "2024-01-30T10:00:00",
                    "sample_description": data.get('sample_description'),
                    "sample_condition": data.get('sample_condition')
                }
            }
            return success_response(response_data, status_code=201)
        except Exception as e:
            return error_response(str(e), 500)


@api.route('/<int:receipt_id>')
@api.param('receipt_id', 'The assessment receipt identifier')
class AssessmentReceiptDetail(Resource):
    @api.doc('get_receipt')
    @api.marshal_with(receipt_model)
    def get(self, receipt_id):
        """Get an assessment receipt by ID"""
        try:
            receipt = {
                "receipt_id": receipt_id,
                "request_id": 1,
                "consultant_staff_id": 3,
                "receive_date": "2024-01-21T09:00:00",
                "sample_description": "Kim cương tròn 1.5 carat, màu D, độ tinh khiết VVS1",
                "sample_condition": "Tốt"
            }
            return success_response({"receipt": receipt})
        except Exception as e:
            return error_response(str(e), 404)
