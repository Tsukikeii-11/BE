"""
AssessmentReceiptService for business logic related to assessment receipts.
"""
from src.infrastructure.repositories.assessment_receipt_repository import AssessmentReceiptRepository
from typing import Dict, Any, Optional, List

class AssessmentReceiptService:
    def __init__(self, receipt_repo: AssessmentReceiptRepository):
        """
        Initializes the AssessmentReceiptService with an AssessmentReceiptRepository.
        """
        self.receipt_repo = receipt_repo
    
    def get_all_receipts(self) -> List[Any]:
        """
        Retrieves all assessment receipts.
        """
        return self.receipt_repo.get_all()

    def create_new_receipt(self, receipt_data: Dict[str, Any]) -> Optional[Any]:
        """
        Creates a new assessment receipt.
        """
        return self.receipt_repo.add(receipt_data)

    def get_receipt_by_id(self, receipt_id: int) -> Optional[Any]:
        """
        Retrieves an assessment receipt by its ID.
        """
        return self.receipt_repo.get_by_id(receipt_id)

    def update_receipt(self, receipt_id: int, update_data: Dict[str, Any]) -> Optional[Any]:
        """
        Updates an existing assessment receipt.
        """
        return self.receipt_repo.update(receipt_id, update_data)

    def delete_receipt(self, receipt_id: int) -> bool:
        """
        Deletes an assessment receipt.
        """
        return self.receipt_repo.delete(receipt_id)
