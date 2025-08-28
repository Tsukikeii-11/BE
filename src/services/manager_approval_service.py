"""
ManagerApprovalService for business logic related to manager approvals.
"""
from src.infrastructure.repositories.manager_approval_repository import ManagerApprovalRepository
from typing import Dict, Any, Optional, List

class ManagerApprovalService:
    def __init__(self, approval_repo: ManagerApprovalRepository):
        """
        Initializes the ManagerApprovalService with a ManagerApprovalRepository.
        """
        self.approval_repo = approval_repo
    
    def get_all_approvals(self) -> List[Any]:
        """
        Retrieves all manager approvals.
        """
        return self.approval_repo.get_all()

    def create_new_approval(self, approval_data: Dict[str, Any]) -> Optional[Any]:
        """
        Creates a new manager approval.
        """
        return self.approval_repo.add(approval_data)

    def get_approval_by_id(self, approval_id: int) -> Optional[Any]:
        """
        Retrieves a manager approval by its ID.
        """
        return self.approval_repo.get_by_id(approval_id)

    def update_approval(self, approval_id: int, update_data: Dict[str, Any]) -> Optional[Any]:
        """
        Updates an existing manager approval.
        """
        return self.approval_repo.update(approval_id, update_data)

    def delete_approval(self, approval_id: int) -> bool:
        """
        Deletes a manager approval.
        """
        return self.approval_repo.delete(approval_id)
