"""
Certificate database model.
This model represents a diamond certification document, mapped directly to the database.
"""
from src.infrastructure.databases.database import db
from sqlalchemy.sql import func
from sqlalchemy import Numeric

class Certificate(db.Model):
    __tablename__ = 'Certificates'
    
    certificate_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    assessment_id = db.Column(db.Integer, db.ForeignKey('AssessmentResults.assessment_id'), nullable=False, unique=True)
    issue_date = db.Column(db.DateTime, default=func.now())
    price = db.Column(Numeric(10, 2), nullable=False)
    certificate_code = db.Column(db.String(100), unique=True, nullable=False)

    # Relationships
    assessment_result = db.relationship('AssessmentResult', backref='certificate', uselist=False)

    def __repr__(self):
        return f"<Certificate(certificate_id={self.certificate_id}, certificate_code='{self.certificate_code}')>"
