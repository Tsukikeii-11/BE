"""
User database models.
These models map directly to the database tables for users and their related entities.
"""
from src.infrastructure.databases.database import db
from sqlalchemy.sql import func

class Role(db.Model):
    __tablename__ = 'Roles'
    
    role_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(50), unique=True, nullable=False)

    # Relationships
    users = db.relationship('User', back_populates='role')

    def __repr__(self):
        return f"<Role(role_name='{self.role_name}')>"

class UserProfile(db.Model):
    __tablename__ = 'UserProfiles'
    
    profile_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20))
    address = db.Column(db.String(255))
    
    # Relationship
    user = db.relationship('User', back_populates='profile', uselist=False)
    assessment_results = db.relationship('AssessmentResult', backref='assessor_profile', lazy=True)
    manager_approvals = db.relationship('ManagerApproval', backref='manager_profile', lazy=True)

    def __repr__(self):
        return f"<UserProfile(full_name='{self.full_name}')>"

class User(db.Model):
    __tablename__ = 'Users'
    
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=func.now())
    
    # Foreign Keys
    profile_id = db.Column(db.Integer, db.ForeignKey('UserProfiles.profile_id'))
    role_id = db.Column(db.Integer, db.ForeignKey('Roles.role_id'))
    
    # Relationships
    profile = db.relationship('UserProfile', back_populates='user')
    role = db.relationship('Role', back_populates='users')
    
    def __repr__(self):
        return f"<User(username='{self.username}')>"
