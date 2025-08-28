"""
SQL Server database connector.
This class handles the connection and session management for Microsoft SQL Server.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.infrastructure.databases.base import Base

class MSSQLDatabase(Base):
    """
    Concrete implementation for connecting to a Microsoft SQL Server database.
    """
    def __init__(self, connection_string: str):
        """
        Initializes the database engine and session factory.
        
        Args:
            connection_string (str): The connection string for the SQL Server database.
        """
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)
        
    def get_session(self):
        """
        Returns a new session for interacting with the database.
        
        Returns:
            A SQLAlchemy Session object.
        """
        return self.Session()
        
    def close_session(self, session):
        """
        Closes the given database session.
        
        Args:
            session: The SQLAlchemy Session object to close.
        """
        session.close()

# Example Usage (optional)
# if __name__ == "__main__":
#     # Thay đổi chuỗi kết nối của bạn tại đây
#     # Ví dụ: 'mssql+pyodbc://user:password@server_name/database_name?driver=ODBC+Driver+17+for+SQL+Server'
#     CONNECTION_STRING = "mssql+pyodbc://..."
#     
#     db_connector = MSSQLDatabase(CONNECTION_STRING)
#     session = db_connector.get_session()
#     
#     try:
#         # Thực hiện các truy vấn của bạn tại đây
#         print("Successfully connected to the database.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         db_connector.close_session(session)
