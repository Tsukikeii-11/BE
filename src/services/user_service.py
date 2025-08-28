"""
UserService for business logic related to users.
"""
from src.infrastructure.repositories.user_repository import UserRepository
from typing import Dict, Any, Optional

class UserService:
    def __init__(self, user_repo: UserRepository):
        """
        Initializes the UserService with a UserRepository.
        """
        self.user_repo = user_repo

    def create_new_user(self, user_data: Dict[str, Any]) -> Optional[Any]:
        """
        Creates a new user account.
        
        Args:
            user_data: A dictionary containing user information.
        
        Returns:
            The created user object, or None if creation failed.
        """
        # Business logic can be added here, e.g., password hashing, validation
        
        # Check if username or email already exists
        existing_user = self.user_repo.get_by_username(user_data.get('username'))
        if existing_user:
            # Handle username conflict
            return None
        
        # Add the new user to the repository
        return self.user_repo.add(user_data)

    def get_user_by_id(self, user_id: int) -> Optional[Any]:
        """
        Retrieves a user by their ID.
        """
        return self.user_repo.get_by_id(user_id)
        
    def get_user_by_username(self, username: str) -> Optional[Any]:
        """
        Retrieves a user by their username.
        """
        return self.user_repo.get_by_username(username)

    def update_user_profile(self, user_id: int, update_data: Dict[str, Any]) -> Optional[Any]:
        """
        Updates an existing user's profile information.
        """
        return self.user_repo.update(user_id, update_data)

    def delete_user(self, user_id: int) -> bool:
        """
        Deletes a user account.
        """
        return self.user_repo.delete(user_id)
