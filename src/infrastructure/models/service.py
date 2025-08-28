"""
Service database model.
This model maps directly to the database table for services.
"""
from src.infrastructure.databases.database import db
from sqlalchemy import Numeric

class Service(db.Model):
    __tablename__ = 'Services'

    service_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(Numeric(10, 2), nullable=False)
    estimated_duration_days = db.Column(db.Integer)
    
    # Relationships
    assessment_requests = db.relationship('AssessmentRequest', back_populates='service')

    def __repr__(self):
        return f"<Service(service_name='{self.service_name}')>"
