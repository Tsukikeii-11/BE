from .mssql import init_mssql
from src.infrastructure.models import todo_model

def init_db(app):
    init_mssql(app)