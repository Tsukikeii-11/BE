"""
A simple dependency injection container using a dictionary.
This helps manage and inject dependencies throughout the application.
"""
from src.infrastructure.repositories.user_repository import UserRepository
from src.infrastructure.repositories.service_repository import ServiceRepository
from src.infrastructure.repositories.assessment_request_repository import AssessmentRequestRepository
from src.infrastructure.repositories.assessment_receipt_repository import AssessmentReceiptRepository
from src.infrastructure.repositories.assessment_result_repository import AssessmentResultRepository
from src.infrastructure.repositories.certificate_repository import CertificateRepository
from src.infrastructure.repositories.manager_approval_repository import ManagerApprovalRepository
from src.services.user_service import UserService
from src.services.service_service import ServiceService
from src.services.assessment_request_service import AssessmentRequestService
from src.services.assessment_receipt_service import AssessmentReceiptService
from src.services.assessment_result_service import AssessmentResultService
from src.services.certificate_service import CertificateService
from src.services.manager_approval_service import ManagerApprovalService

# The container dictionary to hold instances of our dependencies
container = {}

def initialize_container():
    """
    Initializes the dependency injection container with all required instances.
    This function should be called once at application startup.
    """
    # Initialize repositories
    user_repo = UserRepository()
    service_repo = ServiceRepository()
    assessment_request_repo = AssessmentRequestRepository()
    assessment_receipt_repo = AssessmentReceiptRepository()
    assessment_result_repo = AssessmentResultRepository()
    certificate_repo = CertificateRepository()
    manager_approval_repo = ManagerApprovalRepository()

    # Initialize services with their respective repositories
    user_service = UserService(user_repo)
    service_service = ServiceService(service_repo)
    assessment_request_service = AssessmentRequestService(assessment_request_repo)
    assessment_receipt_service = AssessmentReceiptService(assessment_receipt_repo)
    assessment_result_service = AssessmentResultService(assessment_result_repo)
    certificate_service = CertificateService(certificate_repo)
    manager_approval_service = ManagerApprovalService(manager_approval_repo)

    # Store the instances in the container
    container['user_repo'] = user_repo
    container['service_repo'] = service_repo
    container['assessment_request_repo'] = assessment_request_repo
    container['assessment_receipt_repo'] = assessment_receipt_repo
    container['assessment_result_repo'] = assessment_result_repo
    container['certificate_repo'] = certificate_repo
    container['manager_approval_repo'] = manager_approval_repo
    container['user_service'] = user_service
    container['service_service'] = service_service
    container['assessment_request_service'] = assessment_request_service
    container['assessment_receipt_service'] = assessment_receipt_service
    container['assessment_result_service'] = assessment_result_service
    container['certificate_service'] = certificate_service
    container['manager_approval_service'] = manager_approval_service

def get_dependency(name: str):
    """
    Retrieves a dependency from the container.

    Args:
        name (str): The name of the dependency to retrieve.

    Returns:
        The dependency instance.

    Raises:
        KeyError: If the dependency is not found in the container.
    """
    if name not in container:
        raise KeyError(f"Dependency '{name}' not found in the container.")
    return container[name]
