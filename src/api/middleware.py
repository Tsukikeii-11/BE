"""
This module defines middleware functions that handle cross-cutting concerns
such as request logging, adding custom headers, etc.
"""
from flask import request, current_app

def log_request_info(app):
    """
    Logs detailed information about the incoming request before processing.
    """
    @app.before_request
    def log_before_request():
        current_app.logger.info(f"Incoming request: {request.method} {request.path}")
        current_app.logger.debug(f"Headers: {request.headers}")
        try:
            if request.is_json:
                current_app.logger.debug(f"JSON Body: {request.json}")
            else:
                current_app.logger.debug(f"Raw Body: {request.get_data()}")
        except Exception as e:
            current_app.logger.error(f"Error logging request body: {e}")

def add_custom_headers(app):
    """
    Adds a custom header to every response.
    """
    @app.after_request
    def add_headers(response):
        response.headers['X-Api-Version'] = '1.0'
        return response

def register_middleware(app):
    """
    Registers all middleware functions with the Flask application.
    """
    log_request_info(app)
    add_custom_headers(app)
