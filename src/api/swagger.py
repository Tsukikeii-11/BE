"""
Swagger/OpenAPI documentation setup using Flask-RESTX.
This module creates and initializes the API namespaces for documentation.
"""
from flask_restx import Api

api = Api(
    version='1.0.0',
    title='Diamond Assessment System API',
    description='A comprehensive API for managing diamond assessment services including users, services, assessment requests, results, certificates, and approvals.',
    doc='/docs',
    authorizations={
        'apikey': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': "Type 'Bearer <JWT>' where JWT is the token"
        }
    },
    security='apikey'
)

def init_swagger_docs(app):
    """
    Initializes and registers the Flask-RESTX API with the Flask application.
    
    Args:
        app: The Flask application instance.
    """
    # Import the namespace objects from your controller files
    from api.controllers.user_controller import api as user_ns
    from api.controllers.service_controller import api as service_ns
    from api.controllers.assessment_request_controller import api as assessment_request_ns
    from api.controllers.assessment_receipt_controller import api as assessment_receipt_ns
    from api.controllers.assessment_result_controller import api as assessment_result_ns
    from api.controllers.certificate_controller import api as certificate_ns
    from api.controllers.manager_approval_controller import api as manager_approval_ns

    # Add each namespace to the main API
    api.add_namespace(user_ns, path='/api/users')
    api.add_namespace(service_ns, path='/api/services')
    api.add_namespace(assessment_request_ns, path='/api/requests')
    api.add_namespace(assessment_receipt_ns, path='/api/receipts')
    api.add_namespace(assessment_result_ns, path='/api/results')
    api.add_namespace(certificate_ns, path='/api/certificates')
    api.add_namespace(manager_approval_ns, path='/api/approvals')

    api.init_app(app)
