"""
AssessmentResultService for business logic related to assessment results.
"""
from src.infrastructure.repositories.assessment_result_repository import AssessmentResultRepository
from typing import Dict, Any, Optional, List

class AssessmentResultService:
    def __init__(self, result_repo: AssessmentResultRepository):
        """
        Initializes the AssessmentResultService with an AssessmentResultRepository.
        """
        self.result_repo = result_repo
    
    def get_all_results(self) -> List[Any]:
        """
        Retrieves all assessment results.
        """
        return self.result_repo.get_all()

    def create_new_result(self, result_data: Dict[str, Any]) -> Optional[Any]:
        """
        Creates a new assessment result.
        """
        return self.result_repo.add(result_data)

    def get_result_by_id(self, result_id: int) -> Optional[Any]:
        """
        Retrieves an assessment result by its ID.
        """
        return self.result_repo.get_by_id(result_id)

    def update_result(self, result_id: int, update_data: Dict[str, Any]) -> Optional[Any]:
        """
        Updates an existing assessment result.
        """
        return self.result_repo.update(result_id, update_data)

    def delete_result(self, result_id: int) -> bool:
        """
        Deletes an assessment result.
        """
        return self.result_repo.delete(result_id)
