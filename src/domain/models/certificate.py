"""
Domain model for Certificate.
This model represents a diamond certification document, independent of the database.
"""
from typing import Optional
from datetime import datetime
from src.domain.models.assessment_result import AssessmentResult

class Certificate:
    """Represents a certificate for a diamond."""
    def __init__(
        self,
        certificate_id: int,
        assessment_id: int,
        issue_date: datetime,
        price: float,
        certificate_code: str,
    ):
        self.certificate_id = certificate_id
        self.assessment_id = assessment_id
        self.issue_date = issue_date
        self.price = price
        self.certificate_code = certificate_code
        self.assessment_result: Optional[AssessmentResult] = None

    def set_assessment_result(self, assessment_result: AssessmentResult):
        """Sets the assessment result object associated with this certificate."""
        self.assessment_result = assessment_result
