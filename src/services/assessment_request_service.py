"""
AssessmentRequestService for business logic related to assessment requests.
"""
from src.infrastructure.repositories.assessment_request_repository import AssessmentRequestRepository
from typing import Dict, Any, Optional, List

class AssessmentRequestService:
    def __init__(self, request_repo: AssessmentRequestRepository):
        """
        Initializes the AssessmentRequestService with an AssessmentRequestRepository.
        """
        self.request_repo = request_repo
    
    def get_all_requests(self) -> List[Any]:
        """
        Retrieves all assessment requests.
        """
        return self.request_repo.get_all()

    def create_new_request(self, request_data: Dict[str, Any]) -> Optional[Any]:
        """
        Creates a new assessment request.
        """
        return self.request_repo.add(request_data)

    def get_request_by_id(self, request_id: int) -> Optional[Any]:
        """
        Retrieves an assessment request by its ID.
        """
        return self.request_repo.get_by_id(request_id)

    def update_request(self, request_id: int, update_data: Dict[str, Any]) -> Optional[Any]:
        """
        Updates an existing assessment request.
        """
        return self.request_repo.update(request_id, update_data)

    def delete_request(self, request_id: int) -> bool:
        """
        Deletes an assessment request.
        """
        return self.request_repo.delete(request_id)
