"""
Domain models for User, Role, and UserProfile.
These models represent the core business entities, independent of the database.
"""
from typing import Optional
from datetime import datetime

class Role:
    """Represents a user's role in the system."""
    def __init__(self, role_id: int, role_name: str):
        self.role_id = role_id
        self.role_name = role_name

class UserProfile:
    """Represents a user's personal profile information."""
    def __init__(
        self,
        profile_id: int,
        full_name: str,
        phone_number: Optional[str],
        address: Optional[str],
    ):
        self.profile_id = profile_id
        self.full_name = full_name
        self.phone_number = phone_number
        self.address = address

class User:
    """Represents a user account in the system."""
    def __init__(
        self,
        user_id: int,
        username: str,
        email: str,
        is_active: bool,
        created_at: datetime,
        profile_id: int,
        role_id: int
    ):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.is_active = is_active
        self.created_at = created_at
        self.profile_id = profile_id
        self.role_id = role_id
        self.profile: Optional[UserProfile] = None
        self.role: Optional[Role] = None

    def set_profile(self, profile: UserProfile):
        """Sets the user's profile object."""
        self.profile = profile

    def set_role(self, role: Role):
        """Sets the user's role object."""
        self.role = role
