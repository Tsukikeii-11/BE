"""
AssessmentRequestRepository for handling database operations related to AssessmentRequest.
"""
from src.infrastructure.models.assessment_request import AssessmentRequest
from src.infrastructure.databases.database import db

class AssessmentRequestRepository:
    def __init__(self):
        self.model = AssessmentRequest

    def get_by_id(self, request_id):
        """Retrieves an assessment request by its ID."""
        return self.model.query.get(request_id)

    def get_all(self):
        """Retrieves all assessment requests."""
        return self.model.query.all()

    def add(self, request_data):
        """Adds a new assessment request to the database."""
        try:
            new_request = self.model(**request_data)
            db.session.add(new_request)
            db.session.commit()
            return new_request
        except Exception as e:
            db.session.rollback()
            raise e

    def update(self, request_id, request_data):
        """Updates an existing assessment request."""
        request = self.get_by_id(request_id)
        if request:
            for key, value in request_data.items():
                setattr(request, key, value)
            db.session.commit()
            return request
        return None

    def delete(self, request_id):
        """Deletes an assessment request by its ID."""
        request = self.get_by_id(request_id)
        if request:
            db.session.delete(request)
            db.session.commit()
            return True
        return False
