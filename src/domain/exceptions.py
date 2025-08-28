"""
Domain-specific exceptions.
These exceptions represent business logic errors, independent of the infrastructure layer.
"""

from typing import Any

# --- Base exception ---
class DomainException(Exception):
    """Base class for all domain-specific exceptions."""
    def __init__(self, message: str, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.message = message


# --- Generic domain exceptions ---
class EntityNotFoundException(DomainException):
    """Raised when a specific entity is not found in the domain."""
    def __init__(self, entity_name: str, identifier: Any):
        message = f"{entity_name} with identifier '{identifier}' not found."
        super().__init__(message)
        self.entity_name = entity_name
        self.identifier = identifier

class InvalidDataException(DomainException):
    """Raised when input data is invalid for a domain operation."""
    pass

class UnauthorizedAccessException(DomainException):
    """Raised when a user attempts to access a resource without proper authentication."""
    def __init__(self, message: str = "Access denied due to invalid or missing authentication."):
        super().__init__(message)

class ForbiddenException(DomainException):
    """Raised when a user is authenticated but does not have the necessary permissions."""
    def __init__(self, message: str = "Access denied due to insufficient permissions."):
        super().__init__(message)

class BusinessRuleViolationException(DomainException):
    """Raised when a business rule is violated."""
    pass


# --- Specific domain exceptions ---
# Not found
class RequestNotFoundError(EntityNotFoundException):
    def __init__(self, identifier: Any):
        super().__init__("Request", identifier)

class UserNotFoundError(EntityNotFoundException):
    def __init__(self, identifier: Any):
        super().__init__("User", identifier)

class ServiceNotFoundError(EntityNotFoundException):
    def __init__(self, identifier: Any):
        super().__init__("Service", identifier)


# Already exists
class ReceiptAlreadyExistsError(BusinessRuleViolationException):
    def __init__(self, message: str = "Receipt already exists for this request."):
        super().__init__(message)

class ResultAlreadyExistsError(BusinessRuleViolationException):
    def __init__(self, message: str = "Result already exists for this request."):
        super().__init__(message)

class CertificateAlreadyExistsError(BusinessRuleViolationException):
    def __init__(self, message: str = "Certificate already exists for this request."):
        super().__init__(message)

class ApprovalAlreadyExistsError(BusinessRuleViolationException):
    def __init__(self, message: str = "Manager approval already exists for this request."):
        super().__init__(message)

class UserAlreadyExistsError(BusinessRuleViolationException):
    def __init__(self, message: str = "User with this email or username already exists."):
        super().__init__(message)

class ServiceNameConflictError(BusinessRuleViolationException):
    def __init__(self, message: str = "Service with this name already exists."):
        super().__init__(message)


# Authentication
class InvalidCredentialsError(UnauthorizedAccessException):
    def __init__(self, message: str = "Invalid username or password."):
        super().__init__(message)
