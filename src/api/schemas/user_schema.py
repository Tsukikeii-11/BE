"""
Đây là file schema tổng hợp cho các đối tượng liên quan đến người dùng.
"""
from marshmallow import Schema, fields, validate
from marshmallow.validate import Length, OneOf

# Schema cho vai trò người dùng (để trả về)
class RoleResponseSchema(Schema):
    role_id = fields.Int(dump_only=True)
    role_name = fields.Str(dump_only=True)

# Schema cho tài khoản (để trả về)
class AccountResponseSchema(Schema):
    account_id = fields.Int(dump_only=True)
    username = fields.Str()
    email = fields.Str()
    is_active = fields.Bool()
    created_at = fields.DateTime()

# Schema để đăng ký người dùng mới
class UserRegistrationSchema(Schema):
    full_name = fields.Str(required=True, validate=Length(min=3))
    username = fields.Str(required=True, validate=Length(min=5, max=50))
    password = fields.Str(required=True, validate=Length(min=8))
    email = fields.Email(required=True)
    phone_number = fields.Str(required=True, validate=Length(min=10))
    address = fields.Str(required=False, allow_none=True)
    role_name = fields.Str(required=True, validate=OneOf(['Admin', 'Staff', 'Manager', 'Customer']))

# Schema để đăng nhập
class UserLoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

# Schema cho UserProfile (để trả về)
class UserProfileResponseSchema(Schema):
    profile_id = fields.Int(dump_only=True)
    full_name = fields.Str()
    phone_number = fields.Str()
    address = fields.Str()
    
    # Nested schemas
    account = fields.Nested(AccountResponseSchema)
    role = fields.Nested(RoleResponseSchema)
