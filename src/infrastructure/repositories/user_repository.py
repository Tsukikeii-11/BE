"""
UserRepository for handling database operations related to User, UserProfile, and Role.
"""
from src.infrastructure.models.user import User, UserProfile, Role
from src.infrastructure.databases.database import db

class UserRepository:
    def __init__(self):
        self.model = User
        self.profile_model = UserProfile
        self.role_model = Role

    def get_by_id(self, user_id):
        """Retrieves a user by their ID."""
        return self.model.query.get(user_id)

    def get_by_username(self, username):
        """Retrieves a user by their username."""
        return self.model.query.filter_by(username=username).first()

    def add(self, user_data):
        """Adds a new user to the database."""
        try:
            new_user = self.model(**user_data)
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except Exception as e:
            db.session.rollback()
            raise e

    def update(self, user_id, user_data):
        """Updates an existing user."""
        user = self.get_by_id(user_id)
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            db.session.commit()
            return user
        return None

    def delete(self, user_id):
        """Deletes a user by their ID."""
        user = self.get_by_id(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
