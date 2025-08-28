"""
Domain model for AssessmentRequest.
This model represents an assessment request, independent of the database.
"""
from typing import Optional
from datetime import datetime
from src.domain.models.user import User
from src.domain.models.service import Service

class AssessmentRequest:
    """Represents a customer's request for a diamond assessment."""
    def __init__(
        self,
        request_id: int,
        customer_id: int,
        service_id: int,
        request_date: datetime,
        status: str,
        created_at: datetime,
        updated_at: datetime
    ):
        self.request_id = request_id
        self.customer_id = customer_id
        self.service_id = service_id
        self.request_date = request_date
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.customer: Optional[User] = None
        self.service: Optional[Service] = None

    def set_customer(self, customer: User):
        """Sets the customer object associated with this request."""
        self.customer = customer

    def set_service(self, service: Service):
        """Sets the service object associated with this request."""
        self.service = service
