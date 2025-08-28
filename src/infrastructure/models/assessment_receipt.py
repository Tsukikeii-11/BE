"""
AssessmentReceipt database model.
This model represents a record of a diamond assessment receipt, mapped directly to the database.
"""
from src.infrastructure.databases.database import db
from sqlalchemy.sql import func
from sqlalchemy import Numeric

class AssessmentReceipt(db.Model):
    __tablename__ = 'AssessmentReceipts'
    
    receipt_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    request_id = db.Column(db.Integer, db.ForeignKey('AssessmentRequests.request_id'), nullable=False, unique=True)
    consultant_staff_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
    receive_date = db.Column(db.DateTime, default=func.now())
    
    # Relationships
    assessment_request = db.relationship('AssessmentRequest', back_populates='receipt')
    consultant_staff = db.relationship('User', backref='receipts_consulted')

    def __repr__(self):
        return f"<AssessmentReceipt(receipt_id={self.receipt_id}, request_id={self.request_id})>"
