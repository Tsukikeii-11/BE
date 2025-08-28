"""
Abstract base class for database connections.
"""

from abc import ABC, abstractmethod

class DatabaseBase(ABC):
    """
    Abstract base class for all database connector classes.
    Defines the standard interface for connecting to a database.
    """
    @abstractmethod
    def get_session(self):
        """
        Returns a database session or connection object.
        This method must be implemented by concrete database classes.
        """
        pass
    
    @abstractmethod
    def close_session(self, session):
        """
        Closes the database session or connection.
        This method must be implemented by concrete database classes.
        """
        pass
