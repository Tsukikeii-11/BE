"""
Domain model for AssessmentReceipt.
This model represents a record of a diamond assessment receipt, independent of the database.
"""
from typing import Optional
from datetime import datetime
from src.domain.models.assessment_request import AssessmentRequest

class AssessmentReceipt:
    """Represents a receipt for a diamond assessment request."""
    def __init__(
        self,
        receipt_id: int,
        request_id: int,
        consultant_staff_id: int,
        receive_date: datetime,
    ):
        self.receipt_id = receipt_id
        self.request_id = request_id
        self.consultant_staff_id = consultant_staff_id
        self.receive_date = receive_date
        self.assessment_request: Optional[AssessmentRequest] = None

    def set_assessment_request(self, assessment_request: AssessmentRequest):
        """Sets the assessment request object associated with this receipt."""
        self.assessment_request = assessment_request
