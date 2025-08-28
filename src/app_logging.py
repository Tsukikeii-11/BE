"""
Module for configuring and setting up application logging.
"""
import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging(app):
    """
    Sets up a robust logging configuration for the Flask application.

    Args:
        app (Flask): The Flask application instance.
    """
    # Check if a log handler already exists to prevent duplicate logs
    if not app.logger.handlers:
        # Set the logging level based on the application's config
        log_level = app.config.get('LOG_LEVEL', 'INFO').upper()
        app.logger.setLevel(log_level)

        # Create a formatter for the log messages
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Define the log file path
        log_dir = 'logs'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file_path = os.path.join(log_dir, 'app.log')

        # Create a rotating file handler to manage log file size
        # maxBytes=1048576 (1 MB), backupCount=5 (keeps up to 5 files)
        file_handler = RotatingFileHandler(
            log_file_path, maxBytes=1048576, backupCount=5
        )
        file_handler.setFormatter(formatter)
        
        # Create a console handler for printing logs to the terminal
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # Add the handlers to the application's logger
        app.logger.addHandler(file_handler)
        app.logger.addHandler(console_handler)

    # Log a message to indicate that logging has been set up
    app.logger.info("Application logging has been configured.")
