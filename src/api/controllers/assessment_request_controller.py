# src/api/controllers/assessment_request_controller.py
from typing import Any
from flask import Response
from flask_restx import Namespace, Resource, fields
from api.responses import success_response, error_response
from domain.exceptions import UserNotFoundError, InvalidDataException

# Tạo Namespace cho Assessment Requests
api = Namespace('requests', description='Assessment request management operations')

# Swagger models
request_model = api.model('AssessmentRequest', {
    'request_id': fields.Integer(readonly=True, description='Request ID'),
    'customer_id': fields.Integer(required=True, description='Customer ID'),
    'service_id': fields.Integer(required=True, description='Service ID'),
    'request_date': fields.DateTime(readonly=True, description='Request date'),
    'status': fields.String(required=True, description='Request status', enum=['Pending', 'In Progress', 'Completed', 'Cancelled']),
    'customer_notes': fields.String(required=False, description='Customer notes')
})

request_create_model = api.model('AssessmentRequestCreate', {
    'customer_id': fields.Integer(required=True, description='Customer ID'),
    'service_id': fields.Integer(required=True, description='Service ID'),
    'customer_notes': fields.String(required=False, description='Customer notes')
})

request_update_model = api.model('AssessmentRequestUpdate', {
    'status': fields.String(required=False, description='Request status', enum=['Pending', 'In Progress', 'Completed', 'Cancelled']),
    'customer_notes': fields.String(required=False, description='Customer notes')
})


@api.route('/')
class AssessmentRequestList(Resource):
    @api.doc('list_requests')
    @api.marshal_list_with(request_model)
    def get(self):
        """Get all assessment requests"""
        try:
            # Mock data for demonstration
            requests = [
                {
                    "request_id": 1,
                    "customer_id": 7,
                    "service_id": 1,
                    "request_date": "2024-01-20T10:00:00",
                    "status": "Completed",
                    "customer_notes": "Cần giám định kim cương nhẫn cưới"
                },
                {
                    "request_id": 2,
                    "customer_id": 8,
                    "service_id": 2,
                    "request_date": "2024-01-23T14:30:00",
                    "status": "In Progress",
                    "customer_notes": "Giám định kim cương thô"
                },
                {
                    "request_id": 3,
                    "customer_id": 9,
                    "service_id": 3,
                    "request_date": "2024-01-25T09:15:00",
                    "status": "Pending",
                    "customer_notes": "Giám định kim cương cao cấp cho bảo hiểm"
                }
            ]
            return success_response({"requests": requests})
        except Exception as e:
            return error_response(str(e), 500)

    @api.doc('create_request')
    @api.expect(request_create_model)
    @api.marshal_with(request_model)
    @api.response(201, 'Assessment request created successfully')
    def post(self):
        """Create a new assessment request"""
        try:
            data = api.payload
            # TODO: Validate data and call service
            response_data = {
                "message": "Assessment request created successfully.",
                "request": {
                    "request_id": 4,
                    "customer_id": data.get('customer_id'),
                    "service_id": data.get('service_id'),
                    "request_date": "2024-01-30T11:00:00",
                    "status": "Pending",
                    "customer_notes": data.get('customer_notes')
                }
            }
            return success_response(response_data, status_code=201)
        except InvalidDataException as e:
            return error_response(e.message, 400)
        except Exception as e:
            return error_response(str(e), 500)


@api.route('/<int:request_id>')
@api.param('request_id', 'The assessment request identifier')
class AssessmentRequestDetail(Resource):
    @api.doc('get_request')
    @api.marshal_with(request_model)
    def get(self, request_id):
        """Get an assessment request by ID"""
        try:
            # Mock data for demonstration
            request_data = {
                "request_id": request_id,
                "customer_id": 7,
                "service_id": 1,
                "request_date": "2024-01-20T10:00:00",
                "status": "Completed",
                "customer_notes": "Cần giám định kim cương nhẫn cưới"
            }
            return success_response({"request": request_data})
        except Exception as e:
            return error_response(str(e), 404)

    @api.doc('update_request')
    @api.expect(request_update_model)
    @api.marshal_with(request_model)
    def put(self, request_id):
        """Update an assessment request completely"""
        try:
            data = api.payload
            # TODO: Update request logic
            response_data = {
                "message": "Assessment request updated successfully.",
                "request": {
                    "request_id": request_id,
                    "customer_id": 7,
                    "service_id": 1,
                    "request_date": "2024-01-20T10:00:00",
                    "status": data.get('status', 'Pending'),
                    "customer_notes": data.get('customer_notes', 'Cần giám định kim cương nhẫn cưới')
                }
            }
            return success_response(response_data)
        except Exception as e:
            return error_response(str(e), 404)

    @api.doc('update_request_partial')
    @api.expect(request_update_model)
    @api.marshal_with(request_model)
    def patch(self, request_id):
        """Update an assessment request partially"""
        try:
            data = api.payload
            # TODO: Partial update logic
            response_data = {
                "message": "Assessment request updated successfully.",
                "request": {
                    "request_id": request_id,
                    "customer_id": 7,
                    "service_id": 1,
                    "request_date": "2024-01-20T10:00:00",
                    "status": data.get('status', 'Pending'),
                    "customer_notes": data.get('customer_notes', 'Cần giám định kim cương nhẫn cưới')
                }
            }
            return success_response(response_data)
        except Exception as e:
            return error_response(str(e), 404)

    @api.doc('delete_request')
    def delete(self, request_id):
        """Delete an assessment request"""
        try:
            # TODO: Delete request logic
            return success_response({"message": f"Assessment request {request_id} deleted successfully."})
        except Exception as e:
            return error_response(str(e), 404)
