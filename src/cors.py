"""
Module for configuring Cross-Origin Resource Sharing (CORS).
"""
from flask_cors import CORS

def setup_cors(app):
    """
    Sets up CORS for the Flask application to allow cross-origin requests.

    Args:
        app (Flask): The Flask application instance.
    """
    # Initialize CORS with default settings.
    # This allows all origins, methods, and headers.
    CORS(app)
    app.logger.info("CORS has been enabled for all origins.")

    # Example of a more specific CORS configuration
    # CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
