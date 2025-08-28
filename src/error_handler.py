"""
Centralized error handling module for the Flask application.
This module defines a blueprint to register custom error handlers.
"""
from flask import Blueprint, jsonify
from werkzeug.exceptions import HTTPException

# Create a Blueprint for error handling
error_handlers_bp = Blueprint('error_handlers', __name__)

@error_handlers_bp.app_errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Handles all Werkzeug HTTPExceptions and returns a JSON error response.
    """
    response = jsonify({
        "status": "error",
        "message": e.description,
        "code": e.code
    })
    response.status_code = e.code
    return response

@error_handlers_bp.app_errorhandler(Exception)
def handle_unexpected_exception(e):
    """
    Handles all other unexpected exceptions and returns a generic JSON error response.
    """
    response = jsonify({
        "status": "error",
        "message": "An unexpected error occurred.",
        "code": 500
    })
    response.status_code = 500
    # Log the full traceback for debugging purposes
    # The application logger should be used here, but for simplicity, we'll return a generic message.
    return response
