"""
CertificateService for business logic related to certificates.
"""
from src.infrastructure.repositories.certificate_repository import CertificateRepository
from typing import Dict, Any, Optional, List

class CertificateService:
    def __init__(self, certificate_repo: CertificateRepository):
        """
        Initializes the CertificateService with a CertificateRepository.
        """
        self.certificate_repo = certificate_repo
    
    def get_all_certificates(self) -> List[Any]:
        """
        Retrieves all certificates.
        """
        return self.certificate_repo.get_all()

    def create_new_certificate(self, certificate_data: Dict[str, Any]) -> Optional[Any]:
        """
        Creates a new certificate.
        """
        return self.certificate_repo.add(certificate_data)

    def get_certificate_by_id(self, certificate_id: int) -> Optional[Any]:
        """
        Retrieves a certificate by its ID.
        """
        return self.certificate_repo.get_by_id(certificate_id)
    
    def get_certificate_by_code(self, certificate_code: str) -> Optional[Any]:
        """
        Retrieves a certificate by its code.
        """
        return self.certificate_repo.get_by_code(certificate_code)

    def update_certificate(self, certificate_id: int, update_data: Dict[str, Any]) -> Optional[Any]:
        """
        Updates an existing certificate.
        """
        return self.certificate_repo.update(certificate_id, update_data)

    def delete_certificate(self, certificate_id: int) -> bool:
        """
        Deletes a certificate.
        """
        return self.certificate_repo.delete(certificate_id)
