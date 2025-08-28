"""
AssessmentRequest database model.
This model maps directly to the database table for assessment requests.
"""
from src.infrastructure.databases.database import db
from sqlalchemy.sql import func

class AssessmentRequest(db.Model):
    __tablename__ = 'AssessmentRequests'

    request_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('Services.service_id'), nullable=False)
    request_date = db.Column(db.DateTime, default=func.now())
    status = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    customer = db.relationship('User', backref='assessment_requests', lazy=True)
    service = db.relationship('Service', back_populates='assessment_requests')
    receipt = db.relationship('AssessmentReceipt', back_populates='assessment_request', uselist=False)
    result = db.relationship('AssessmentResult', back_populates='assessment_request', uselist=False)
    manager_approvals = db.relationship('ManagerApproval', back_populates='assessment_request', lazy=True)
    
    def __repr__(self):
        return f"<AssessmentRequest(request_id={self.request_id}, status='{self.status}')>"
