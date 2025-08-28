"""
Domain constants for status codes, messages, etc.
"""

# Common status for assessment requests
ASSESSMENT_REQUEST_STATUS_PENDING = "Pending"
ASSESSMENT_REQUEST_STATUS_APPROVED = "Approved"
ASSESSMENT_REQUEST_STATUS_REJECTED = "Rejected"
ASSESSMENT_REQUEST_STATUS_IN_PROGRESS = "In Progress"
ASSESSMENT_REQUEST_STATUS_COMPLETED = "Completed"

# Common status for receipts
RECEIPT_STATUS_PENDING = "Pending"
RECEIPT_STATUS_PAID = "Paid"

# Common roles
ROLE_ADMIN = "Admin"
ROLE_MANAGER = "Manager"
ROLE_STAFF = "Staff"
ROLE_CUSTOMER = "Customer"

# Common messages
MESSAGE_SUCCESS = "Success"
MESSAGE_FAILURE = "Failure"
MESSAGE_NOT_FOUND = "Resource not found"
MESSAGE_UNAUTHORIZED = "Unauthorized access"
MESSAGE_FORBIDDEN = "Forbidden access"
