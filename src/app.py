"""
Main application factory file for the Flask-CleanArchitecture project.
This file creates and configures the Flask application instance.
"""
from flask import Flask
from infrastructure.databases.database import db
from api.swagger import init_swagger_docs
from cors import setup_cors
from api.middleware import log_request_info, add_custom_headers

def create_app():
    """
    Creates and configures the Flask application.

    Returns:
        The Flask application instance.
    """
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.Config')

    # Setup CORS
    setup_cors(app)

    # Setup middleware
    log_request_info(app)
    add_custom_headers(app)

    # Initialize database
    db.init_app(app)

    # Initialize Swagger documentation
    init_swagger_docs(app)

    # Example of a custom error handler
    @app.errorhandler(404)
    def page_not_found(e):
        return {"error": "The requested resource was not found."}, 404

    @app.errorhandler(400)
    def bad_request(e):
        return {"error": "Bad request. Please check your input."}, 400

    @app.errorhandler(409)
    def conflict(e):
        return {"error": "Conflict. The resource already exists."}, 409

    return app

if __name__ == '__main__':
    # This block is executed when you run the file directly
    app = create_app()

    # Create all database tables (if they don't exist)
    with app.app_context():
        db.create_all()
    
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)
