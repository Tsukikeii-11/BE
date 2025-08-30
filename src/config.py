"""
Configuration settings for the Flask application.
"""
import os

class Config:
    """Base configuration class."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A_SECRET_KEY_THAT_SHOULD_BE_CHANGED_IN_PROD'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///default.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_LEVEL = os.environ.get('LOG_LEVEL') or 'INFO'
    SWAGGER_URL = '/docs'
    API_URL = '/api'
    
    # Flask-RESTX configuration
    RESTX_VALIDATE = True
    RESTX_MASK_SWAGGER = False
    ERROR_404_HELP = False

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

# A dictionary to map configuration names to classes
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
