"""
Domain model for Service.
This model represents a service offering, independent of the database.
"""
from typing import Optional

class Service:
    """Represents a service offered by the company."""
    def __init__(
        self,
        service_id: int,
        service_name: str,
        description: Optional[str],
        price: float,
        estimated_duration_days: int
    ):
        self.service_id = service_id
        self.service_name = service_name
        self.description = description
        self.price = price
        self.estimated_duration_days = estimated_duration_days
