"""
ManagerApprovalRepository for handling database operations related to ManagerApproval.
"""
from src.infrastructure.models.manager_approval import ManagerApproval
from src.infrastructure.databases.database import db

class ManagerApprovalRepository:
    def __init__(self):
        self.model = ManagerApproval

    def get_by_id(self, approval_id):
        """Retrieves a manager approval by its ID."""
        return self.model.query.get(approval_id)

    def get_by_request_id(self, request_id):
        """Retrieves a manager approval by its request ID."""
        return self.model.query.filter_by(request_id=request_id).first()

    def get_all(self):
        """Retrieves all manager approvals."""
        return self.model.query.all()

    def add(self, approval_data):
        """Adds a new manager approval to the database."""
        try:
            new_approval = self.model(**approval_data)
            db.session.add(new_approval)
            db.session.commit()
            return new_approval
        except Exception as e:
            db.session.rollback()
            raise e

    def update(self, approval_id, approval_data):
        """Updates an existing manager approval."""
        approval = self.get_by_id(approval_id)
        if approval:
            for key, value in approval_data.items():
                setattr(approval, key, value)
            db.session.commit()
            return approval
        return None

    def delete(self, approval_id):
        """Deletes a manager approval by its ID."""
        approval = self.get_by_id(approval_id)
        if approval:
            db.session.delete(approval)
            db.session.commit()
            return True
        return False
