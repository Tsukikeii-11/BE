"""
Main application factory file for the Flask-CleanArchitecture project.
This file creates and configures the Flask application instance.
"""
from flask import Flask
from src.infrastructure.databases.database import db
from src.api.swagger import api as swagger_api
from src.domain.exceptions import *

def create_app():
    """
    Creates and configures the Flask application.

    Returns:
        The Flask application instance.
    """
    app = Flask(__name__)

    # Load configuration from config.py
    # app.config.from_object('config.Config')

    # Initialize extensions
    # This is a common pattern to handle circular imports and make the app more testable.
    # The 'db' and 'swagger_api' objects are initialized with the app instance.
    db.init_app(app)
    swagger_api.init_app(app)

    # Note: Flask-RESTX automatically handles API documentation
    # so we don't need flasgger or flask_swagger_ui.

    # Register blueprints (if any are used outside of Flask-RESTX namespaces)
    # from your_module import your_blueprint
    # app.register_blueprint(your_blueprint)

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
    # This is a simple way to set up the database for development.
    with app.app_context():
        db.create_all()
    
    # Run the application
    app.run(debug=True)
