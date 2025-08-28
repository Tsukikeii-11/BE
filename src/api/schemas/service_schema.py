"""
Đây là file schema tổng hợp cho các đối tượng liên quan đến dịch vụ và giám định.
"""
from marshmallow import Schema, fields, validate
from src.api.schemas.user_schema import UserProfileResponseSchema

# Schema cho yêu cầu tạo và cập nhật dịch vụ
class ServiceRequestSchema(Schema):
    service_name = fields.Str(required=True, validate=validate.Length(min=3, max=255))
    description = fields.Str(required=False, allow_none=True)
    price = fields.Decimal(required=True, as_string=False)
    estimated_duration_days = fields.Int(required=True)

# Schema cho phản hồi khi lấy thông tin dịch vụ
class ServiceResponseSchema(Schema):
    service_id = fields.Int(dump_only=True)
    service_name = fields.Str()
    description = fields.Str()
    price = fields.Decimal(as_string=False)
    estimated_duration_days = fields.Int()

# Schema cho yêu cầu tạo một phiếu yêu cầu giám định mới
class AssessmentRequestSchema(Schema):
    customer_id = fields.Int(required=True)
    service_id = fields.Int(required=True)

# Schema cho phản hồi khi lấy thông tin yêu cầu giám định
class AssessmentRequestResponseSchema(Schema):
    request_id = fields.Int(dump_only=True)
    customer_id = fields.Int(dump_only=True)
    service_id = fields.Int(dump_only=True)
    request_date = fields.DateTime(dump_only=True)
    status = fields.Str(dump_only=True)
    
    # Nested schemas để trả về thông tin chi tiết của khách hàng và dịch vụ
    customer = fields.Nested(UserProfileResponseSchema)
    service = fields.Nested(ServiceResponseSchema)

# Schema cho yêu cầu tạo biên nhận giám định
class AssessmentReceiptRequestSchema(Schema):
    request_id = fields.Int(required=True)
    consultant_staff_id = fields.Int(required=True)

# Schema cho phản hồi khi lấy thông tin biên nhận giám định
class AssessmentReceiptResponseSchema(Schema):
    receipt_id = fields.Int(dump_only=True)
    request_id = fields.Int(dump_only=True)
    consultant_staff_id = fields.Int(dump_only=True)
    receive_date = fields.DateTime(dump_only=True)
    
    # Nested schemas
    assessment_request = fields.Nested(AssessmentRequestResponseSchema)
    consultant_staff = fields.Nested(UserProfileResponseSchema)

# Schema cho yêu cầu tạo kết quả giám định
class AssessmentResultRequestSchema(Schema):
    receipt_id = fields.Int(required=True)
    assessor_id = fields.Int(required=True)
    diamond_origin = fields.Str(required=True)
    shape_and_cut = fields.Str(required=True)
    measurements = fields.Str(required=True)
    carat_weight = fields.Decimal(required=True, as_string=False)
    color = fields.Str(required=True)
    clarity = fields.Str(required=True)
    cut = fields.Str(required=True)
    polish = fields.Str(required=True)
    symmetry = fields.Str(required=True)
    fluorescence = fields.Str(required=True)
    comments = fields.Str(required=False, allow_none=True)

# Schema cho phản hồi khi lấy thông tin kết quả giám định
class AssessmentResultResponseSchema(Schema):
    assessment_id = fields.Int(dump_only=True)
    receipt_id = fields.Int(dump_only=True)
    assessor_id = fields.Int(dump_only=True)
    result_date = fields.DateTime(dump_only=True)
    diamond_origin = fields.Str()
    shape_and_cut = fields.Str()
    measurements = fields.Str()
    carat_weight = fields.Decimal(as_string=False)
    color = fields.Str()
    clarity = fields.Str()
    cut = fields.Str()
    polish = fields.Str()
    symmetry = fields.Str()
    fluorescence = fields.Str()
    comments = fields.Str()
    
    # Nested schemas
    assessment_receipt = fields.Nested(AssessmentReceiptResponseSchema)
    assessor = fields.Nested(UserProfileResponseSchema)

# Schema cho yêu cầu tạo phê duyệt của quản lý
class ManagerApprovalRequestSchema(Schema):
    request_id = fields.Int(required=True)
    manager_id = fields.Int(required=True)
    status = fields.Str(required=True, validate=lambda s: s in ['Approved', 'Rejected'])
    comments = fields.Str(required=False, allow_none=True)

# Schema cho phản hồi khi lấy thông tin phê duyệt của quản lý
class ManagerApprovalResponseSchema(Schema):
    approval_id = fields.Int(dump_only=True)
    request_id = fields.Int(dump_only=True)
    manager_id = fields.Int(dump_only=True)
    approval_date = fields.DateTime(dump_only=True)
    status = fields.Str(dump_only=True)
    comments = fields.Str(dump_only=True)
    
    # Nested schemas
    assessment_request = fields.Nested(AssessmentRequestResponseSchema)
    manager = fields.Nested(UserProfileResponseSchema)

# Schema cho yêu cầu tạo giấy chứng nhận
class CertificateRequestSchema(Schema):
    assessment_id = fields.Int(required=True)
    price = fields.Decimal(required=True, as_string=False)
    certificate_code = fields.Str(required=True)

# Schema cho phản hồi khi lấy thông tin giấy chứng nhận
class CertificateResponseSchema(Schema):
    certificate_id = fields.Int(dump_only=True)
    assessment_id = fields.Int(dump_only=True)
    issue_date = fields.DateTime(dump_only=True)
    price = fields.Decimal(as_string=False, dump_only=True)
    certificate_code = fields.Str(dump_only=True)
    
    # Nested schemas
    assessment_result = fields.Nested(AssessmentResultResponseSchema)
