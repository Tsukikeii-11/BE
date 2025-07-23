from domain.models.itodo_repository import ITodoRepository
from domain.models.todo import Todo
from typing import List, Optional
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config
from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases import Base

load_dotenv()

class TodoRepository(ITodoRepository):
    def __init__(self):
        self._todos = []
        self._id_counter = 1

    def add(self, todo: Todo) -> Todo:
        todo.id = self._id_counter
        self._id_counter += 1
        self._todos.append(todo)
        return todo

    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        for todo in self._todos:
            if todo.id == todo_id:
                return todo
        return None

    def list(self) -> List[Todo]:
        return self._todos

    def update(self, todo: Todo) -> Todo:
        for idx, t in enumerate(self._todos):
            if t.id == todo.id:
                self._todos[idx] = todo
                return todo
        raise ValueError('Todo not found')

    def delete(self, todo_id: int) -> None:
        self._todos = [t for t in self._todos if t.id != todo_id] 

class TodoModel(Base):
    __tablename__ = 'todos'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime) 