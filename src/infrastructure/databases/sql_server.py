# src/infrastructure/databases/sql_server.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine import URL
from src.infrastructure.databases.base import Base
from src.infrastructure.models.user import *
from src.infrastructure.models.assessment_receipt import *
from src.infrastructure.models.assessment_request import *
from src.infrastructure.models.assessment_result import *
def create_sql_server_engine(server_name: str, database_name: str):
    """
    Tạo engine kết nối tới cơ sở dữ liệu SQL Server.
    Sử dụng Windows Authentication.
    """
    connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + server_name + ";DATABASE=" + database_name + ";Trusted_Connection=yes;"
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
    return create_engine(connection_url)

def create_db_session(engine) -> Session:
    """
    Tạo một phiên làm việc (session) để tương tác với cơ sở dữ liệu.
    """
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()

def create_tables(engine):
    """
    Tạo các bảng trong cơ sở dữ liệu dựa trên các mô hình ORM.
    """
    Base.metadata.create_all(bind=engine)