"""
Domain model for ManagerApproval.
This model represents a manager's approval or rejection of an assessment request, independent of the database.
"""
from typing import Optional
from datetime import datetime
from src.domain.models.assessment_request import AssessmentRequest
from src.domain.models.user import User

class ManagerApproval:
    """Represents a manager's approval for a request."""
    def __init__(
        self,
        approval_id: int,
        request_id: int,
        manager_id: int,
        approval_date: datetime,
        status: str, # 'Approved' or 'Rejected'
        comments: Optional[str]
    ):
        self.approval_id = approval_id
        self.request_id = request_id
        self.manager_id = manager_id
        self.approval_date = approval_date
        self.status = status
        self.comments = comments
        self.assessment_request: Optional[AssessmentRequest] = None
        self.manager: Optional[User] = None

    def set_assessment_request(self, assessment_request: AssessmentRequest):
        """Sets the assessment request object associated with this approval."""
        self.assessment_request = assessment_request

    def set_manager(self, manager: User):
        """Sets the manager object associated with this approval."""
        self.manager = manager
