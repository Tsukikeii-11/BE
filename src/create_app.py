"""
Main application factory module.
This file contains the create_app function to create and configure the Flask application.
"""
from flask import Flask
from src.config import config_by_name
from src.infrastructure.databases.database import configure_database
from src.app_logging import setup_logging
from src.cors import setup_cors
from src.error_handler import error_handlers_bp
from src.dependency_container import initialize_container
from src.api.swagger import init_swagger_docs

def create_app(config_name):
    """
    Creates and configures a new Flask application.
    
    Args:
        config_name (str): The name of the configuration to use.
    
    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    
    # Load configuration from the specified config class
    app.config.from_object(config_by_name[config_name])
    
    # Configure logging
    setup_logging(app)
    
    # Configure database connection
    configure_database(app)
    
    # Initialize dependency injection container
    initialize_container()
    
    # Set up CORS
    setup_cors(app)
    
    # Register blueprints for error handling and APIs
    app.register_blueprint(error_handlers_bp)

    # Initialize and register Swagger docs
    init_swagger_docs(app)

    # Note: Flask-RESTX handles the blueprint registration via `api.add_namespace`,
    # which is called inside `init_swagger_docs`. No need to call register_blueprint here.
    
    app.logger.info("Application created successfully.")
    
    return app
