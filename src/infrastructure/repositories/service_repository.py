"""
ServiceRepository for handling database operations related to Service.
"""
from src.infrastructure.models.service import Service
from src.infrastructure.databases.database import db

class ServiceRepository:
    def __init__(self):
        self.model = Service

    def get_by_id(self, service_id):
        """Retrieves a service by its ID."""
        return self.model.query.get(service_id)

    def get_all(self):
        """Retrieves all services."""
        return self.model.query.all()

    def get_by_name(self, service_name):
        """Retrieves a service by its name."""
        return self.model.query.filter_by(service_name=service_name).first()

    def add(self, service_data):
        """Adds a new service to the database."""
        try:
            new_service = self.model(**service_data)
            db.session.add(new_service)
            db.session.commit()
            return new_service
        except Exception as e:
            db.session.rollback()
            raise e

    def update(self, service_id, service_data):
        """Updates an existing service."""
        service = self.get_by_id(service_id)
        if service:
            for key, value in service_data.items():
                setattr(service, key, value)
            db.session.commit()
            return service
        return None

    def delete(self, service_id):
        """Deletes a service by its ID."""
        service = self.get_by_id(service_id)
        if service:
            db.session.delete(service)
            db.session.commit()
            return True
        return False
