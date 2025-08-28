"""
ManagerApproval database model.
This model represents a manager's approval or rejection of an assessment request.
"""
from src.infrastructure.databases.database import db
from sqlalchemy.sql import func

class ManagerApproval(db.Model):
    __tablename__ = 'ManagerApprovals'

    approval_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    request_id = db.Column(db.Integer, db.ForeignKey('AssessmentRequests.request_id'), nullable=False, unique=True)
    manager_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
    approval_date = db.Column(db.DateTime, default=func.now())
    status = db.Column(db.String(50), nullable=False)  # 'Approved' or 'Rejected'
    comments = db.Column(db.String(255))
    
    # Relationships
    assessment_request = db.relationship('AssessmentRequest', back_populates='manager_approvals')
    manager = db.relationship('User', backref='manager_approvals')

    def __repr__(self):
        return f"<ManagerApproval(approval_id={self.approval_id}, status='{self.status}')>"
