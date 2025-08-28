"""
This module handles the database connection and configuration using SQLAlchemy.
It is designed to work with SQL Server.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure_database(app):
    """
    Configures the SQLAlchemy database for the Flask application.
    
    Args:
        app (Flask): The Flask application instance.
    """
    # Use environment variable for the connection string, or a default
    # The connection string for SQL Server with Windows Authentication is
    # 'mssql+pyodbc://<server_name>/<database_name>?driver=ODBC+Driver+17+for+SQL+Server'
    
    # It's highly recommended to use environment variables for production
    # For local development with Windows Authentication, you can use a fixed string
    server_name = app.config.get('DB_SERVER_NAME', 'TuanDepzai')
    db_name = app.config.get('DB_NAME', 'DiamondDB')
    
    # Connection string using pyodbc with Windows Authentication
    # Note: Ensure 'ODBC Driver 17 for SQL Server' is installed on your machine.
    connection_string = f'mssql+pyodbc://{server_name}/{db_name}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    # Note: To create tables from your models, you will need to run
    # db.create_all() inside an application context. This is typically done
    # in a separate script or a shell.
    #
    # Example to run in a Flask shell:
    # >>> from src.create_app import create_app
    # >>> from src.infrastructure.database.database import db
    # >>> from src.infrastructure.models.user import User  # import all models
    # >>> app = create_app('development')
    # >>> app.app_context().push()
    # >>> db.create_all()
