"""
AssessmentResultRepository for handling database operations related to AssessmentResult.
"""
from src.infrastructure.models.assessment_result import AssessmentResult
from src.infrastructure.databases.database import db

class AssessmentResultRepository:
    def __init__(self):
        self.model = AssessmentResult

    def get_by_id(self, assessment_id):
        """Retrieves an assessment result by its ID."""
        return self.model.query.get(assessment_id)

    def get_all(self):
        """Retrieves all assessment results."""
        return self.model.query.all()

    def add(self, result_data):
        """Adds a new assessment result to the database."""
        try:
            new_result = self.model(**result_data)
            db.session.add(new_result)
            db.session.commit()
            return new_result
        except Exception as e:
            db.session.rollback()
            raise e

    def update(self, assessment_id, result_data):
        """Updates an existing assessment result."""
        result = self.get_by_id(assessment_id)
        if result:
            for key, value in result_data.items():
                setattr(result, key, value)
            db.session.commit()
            return result
        return None

    def delete(self, assessment_id):
        """Deletes an assessment result by its ID."""
        result = self.get_by_id(assessment_id)
        if result:
            db.session.delete(result)
            db.session.commit()
            return True
        return False
