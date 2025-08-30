# src/api/controllers/assessment_result_controller.py
from flask_restx import Namespace, Resource, fields
from api.responses import success_response, error_response

api = Namespace('results', description='Assessment result management operations')

result_model = api.model('AssessmentResult', {
    'assessment_id': fields.Integer(readonly=True, description='Assessment ID'),
    'receipt_id': fields.Integer(required=True, description='Receipt ID'),
    'assessor_id': fields.Integer(required=True, description='Assessor ID'),
    'result_date': fields.DateTime(readonly=True, description='Result date'),
    'carat_weight': fields.Float(required=True, description='Carat weight'),
    'color': fields.String(required=True, description='Color grade'),
    'clarity': fields.String(required=True, description='Clarity grade'),
    'cut': fields.String(required=True, description='Cut grade'),
    'comments': fields.String(required=False, description='Assessment comments')
})


@api.route('/')
class AssessmentResultList(Resource):
    @api.doc('list_results')
    @api.marshal_list_with(result_model)
    def get(self):
        """Get all assessment results"""
        try:
            results = [
                {
                    "assessment_id": 1,
                    "receipt_id": 1,
                    "assessor_id": 5,
                    "result_date": "2024-01-23T15:00:00",
                    "carat_weight": 1.52,
                    "color": "D",
                    "clarity": "VVS1",
                    "cut": "Excellent",
                    "comments": "Kim cương chất lượng cao"
                }
            ]
            return success_response({"results": results})
        except Exception as e:
            return error_response(str(e), 500)


@api.route('/<int:result_id>')
@api.param('result_id', 'The assessment result identifier')
class AssessmentResultDetail(Resource):
    @api.doc('get_result')
    @api.marshal_with(result_model)
    def get(self, result_id):
        """Get an assessment result by ID"""
        try:
            result = {
                "assessment_id": result_id,
                "receipt_id": 1,
                "assessor_id": 5,
                "result_date": "2024-01-23T15:00:00",
                "carat_weight": 1.52,
                "color": "D",
                "clarity": "VVS1",
                "cut": "Excellent",
                "comments": "Kim cương chất lượng cao"
            }
            return success_response({"result": result})
        except Exception as e:
            return error_response(str(e), 404)
