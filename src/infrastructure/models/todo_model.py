from sqlalchemy import Column, Integer, String, DateTime
from src.infrastructure.databases.base import Base

class TodoModel(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime) 