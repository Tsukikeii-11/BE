"""
ServiceService for business logic related to services.
"""
from src.infrastructure.repositories.service_repository import ServiceRepository
from typing import Dict, Any, Optional, List

class ServiceService:
    def __init__(self, service_repo: ServiceRepository):
        """
        Initializes the ServiceService with a ServiceRepository.
        """
        self.service_repo = service_repo
    
    def get_all_services(self) -> List[Any]:
        """
        Retrieves all services.
        """
        return self.service_repo.get_all()

    def create_new_service(self, service_data: Dict[str, Any]) -> Optional[Any]:
        """
        Creates a new service.
        """
        return self.service_repo.add(service_data)

    def get_service_by_id(self, service_id: int) -> Optional[Any]:
        """
        Retrieves a service by its ID.
        """
        return self.service_repo.get_by_id(service_id)

    def update_service(self, service_id: int, update_data: Dict[str, Any]) -> Optional[Any]:
        """
        Updates an existing service.
        """
        return self.service_repo.update(service_id, update_data)

    def delete_service(self, service_id: int) -> bool:
        """
        Deletes a service.
        """
        return self.service_repo.delete(service_id)
