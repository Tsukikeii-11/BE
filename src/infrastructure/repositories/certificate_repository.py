"""
CertificateRepository for handling database operations related to Certificate.
"""
from src.infrastructure.models.certificate import Certificate
from src.infrastructure.databases.database import db

class CertificateRepository:
    def __init__(self):
        self.model = Certificate

    def get_by_id(self, certificate_id):
        """Retrieves a certificate by its ID."""
        return self.model.query.get(certificate_id)

    def get_all(self):
        """Retrieves all certificates."""
        return self.model.query.all()

    def get_by_code(self, certificate_code):
        """Retrieves a certificate by its code."""
        return self.model.query.filter_by(certificate_code=certificate_code).first()

    def add(self, certificate_data):
        """Adds a new certificate to the database."""
        try:
            new_certificate = self.model(**certificate_data)
            db.session.add(new_certificate)
            db.session.commit()
            return new_certificate
        except Exception as e:
            db.session.rollback()
            raise e

    def update(self, certificate_id, certificate_data):
        """Updates an existing certificate."""
        certificate = self.get_by_id(certificate_id)
        if certificate:
            for key, value in certificate_data.items():
                setattr(certificate, key, value)
            db.session.commit()
            return certificate
        return None

    def delete(self, certificate_id):
        """Deletes a certificate by its ID."""
        certificate = self.get_by_id(certificate_id)
        if certificate:
            db.session.delete(certificate)
            db.session.commit()
            return True
        return False
