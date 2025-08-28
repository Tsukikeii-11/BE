"""
AssessmentReceiptRepository for handling database operations related to AssessmentReceipt.
"""
from src.infrastructure.models.assessment_receipt import AssessmentReceipt
from src.infrastructure.databases.database import db

class AssessmentReceiptRepository:
    def __init__(self):
        self.model = AssessmentReceipt

    def get_by_id(self, receipt_id):
        """Retrieves an assessment receipt by its ID."""
        return self.model.query.get(receipt_id)

    def get_all(self):
        """Retrieves all assessment receipts."""
        return self.model.query.all()

    def add(self, receipt_data):
        """Adds a new assessment receipt to the database."""
        try:
            new_receipt = self.model(**receipt_data)
            db.session.add(new_receipt)
            db.session.commit()
            return new_receipt
        except Exception as e:
            db.session.rollback()
            raise e

    def update(self, receipt_id, receipt_data):
        """Updates an existing assessment receipt."""
        receipt = self.get_by_id(receipt_id)
        if receipt:
            for key, value in receipt_data.items():
                setattr(receipt, key, value)
            db.session.commit()
            return receipt
        return None

    def delete(self, receipt_id):
        """Deletes an assessment receipt by its ID."""
        receipt = self.get_by_id(receipt_id)
        if receipt:
            db.session.delete(receipt)
            db.session.commit()
            return True
        return False
