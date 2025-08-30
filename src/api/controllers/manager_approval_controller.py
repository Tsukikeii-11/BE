# src/api/controllers/manager_approval_controller.py
from flask_restx import Namespace, Resource, fields
from api.responses import success_response, error_response

api = Namespace('approvals', description='Manager approval operations')

approval_model = api.model('ManagerApproval', {
    'approval_id': fields.Integer(readonly=True, description='Approval ID'),
    'request_id': fields.Integer(required=True, description='Request ID'),
    'manager_id': fields.Integer(required=True, description='Manager ID'),
    'approval_date': fields.DateTime(readonly=True, description='Approval date'),
    'status': fields.String(required=True, description='Approval status', enum=['Approved', 'Rejected', 'Pending']),
    'comments': fields.String(required=False, description='Approval comments'),
    'approval_type': fields.String(required=True, description='Approval type')
})


@api.route('/')
class ManagerApprovalList(Resource):
    @api.doc('list_approvals')
    @api.marshal_list_with(approval_model)
    def get(self):
        """Get all manager approvals"""
        try:
            approvals = [
                {
                    "approval_id": 1,
                    "request_id": 1,
                    "manager_id": 2,
                    "approval_date": "2024-01-22T14:00:00",
                    "status": "Approved",
                    "comments": "Phê duyệt giám định kim cương nhẫn cưới",
                    "approval_type": "Assessment"
                }
            ]
            return success_response({"approvals": approvals})
        except Exception as e:
            return error_response(str(e), 500)


@api.route('/<int:approval_id>')
@api.param('approval_id', 'The manager approval identifier')
class ManagerApprovalDetail(Resource):
    @api.doc('get_approval')
    @api.marshal_with(approval_model)
    def get(self, approval_id):
        """Get a manager approval by ID"""
        try:
            approval = {
                "approval_id": approval_id,
                "request_id": 1,
                "manager_id": 2,
                "approval_date": "2024-01-22T14:00:00",
                "status": "Approved",
                "comments": "Phê duyệt giám định kim cương nhẫn cưới",
                "approval_type": "Assessment"
            }
            return success_response({"approval": approval})
        except Exception as e:
            return error_response(str(e), 404)
