"""
Module to generate standardized API responses.
This helps maintain a consistent JSON response format across the application.
"""
from flask import jsonify
from typing import Dict, Any, Union, List

def success_response(data: Union[Dict, List, None], message: str = "Success", status_code: int = 200):
    """
    Generates a standardized success response in JSON format.
    
    Args:
        data: The payload to be returned. Can be a dictionary, list, etc.
        message (str): A message describing the success.
        status_code (int): The HTTP status code.
        
    Returns:
        A Flask Response object with the JSON payload and status code.
    """
    response_payload = {
        "status": "success",
        "message": message,
        "data": data
    }
    return jsonify(response_payload), status_code

def error_response(message: str, status_code: int = 400):
    """
    Generates a standardized error response in JSON format.
    
    Args:
        message (str): An error message.
        status_code (int): The HTTP status code.
        
    Returns:
        A Flask Response object with the JSON payload and status code.
    """
    response_payload = {
        "status": "error",
        "message": message
    }
    return jsonify(response_payload), status_code
