"""
Domain model for AssessmentResult.
This model represents the final result of a diamond assessment, independent of the database.
"""
from typing import Optional
from datetime import datetime

class AssessmentResult:
    """Represents the detailed result of a diamond assessment."""
    def __init__(
        self,
        assessment_id: int,
        receipt_id: int,
        assessor_id: int,
        result_date: datetime,
        diamond_origin: Optional[str] = None,
        shape_and_cut: Optional[str] = None,
        measurements: Optional[str] = None,
        carat_weight: Optional[float] = None,
        color: Optional[str] = None,
        clarity: Optional[str] = None,
        cut: Optional[str] = None,
        polish: Optional[str] = None,
        symmetry: Optional[str] = None,
        fluorescence: Optional[str] = None,
        comments: Optional[str] = None
    ):
        self.assessment_id = assessment_id
        self.receipt_id = receipt_id
        self.assessor_id = assessor_id
        self.result_date = result_date
        self.diamond_origin = diamond_origin
        self.shape_and_cut = shape_and_cut
        self.measurements = measurements
        self.carat_weight = carat_weight
        self.color = color
        self.clarity = clarity
        self.cut = cut
        self.polish = polish
        self.symmetry = symmetry
        self.fluorescence = fluorescence
        self.comments = comments
