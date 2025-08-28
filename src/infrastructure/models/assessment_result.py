"""
AssessmentResult database model.
This model represents the final result of a diamond assessment, mapped directly to the database.
"""
from src.infrastructure.databases.database import db
from sqlalchemy.sql import func
from sqlalchemy import Numeric

class AssessmentResult(db.Model):
    __tablename__ = 'AssessmentResults'
    
    assessment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    receipt_id = db.Column(db.Integer, db.ForeignKey('AssessmentReceipts.receipt_id'), nullable=False, unique=True)
    assessor_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
    result_date = db.Column(db.DateTime, default=func.now())
    diamond_origin = db.Column(db.String(100))
    shape_and_cut = db.Column(db.String(100))
    measurements = db.Column(db.String(100))
    carat_weight = db.Column(Numeric(10, 2), nullable=False)
    color = db.Column(db.String(50))
    clarity = db.Column(db.String(50))
    cut = db.Column(db.String(50))
    polish = db.Column(db.String(50))
    symmetry = db.Column(db.String(50))
    fluorescence = db.Column(db.String(50))
    comments = db.Column(db.String(255))

    # Relationships
    assessment_receipt = db.relationship('AssessmentReceipt', back_populates='result')
    assessor = db.relationship('User', backref='assessment_results')

    def __repr__(self):
        return f"<AssessmentResult(assessment_id={self.assessment_id}, receipt_id={self.receipt_id})>"
