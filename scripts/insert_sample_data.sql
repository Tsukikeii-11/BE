-- =====================================================
-- INSERT DỮ LIỆU MẪU CHO DIAMOND ASSESSMENT SYSTEM
-- Database: DiamondDB
-- =====================================================

USE DiamondDB;
GO

-- =====================================================
-- 1. INSERT USER PROFILES (Thông tin cá nhân)
-- =====================================================

-- Admin Profile
INSERT INTO UserProfiles (full_name, phone_number, email, address, id_card_number, date_of_birth, gender)
VALUES 
('Nguyễn Văn Admin', '0901234567', 'admin@diamond.com', '123 Đường ABC, Quận 1, TP.HCM', '123456789012', '1980-01-01', 'Nam');

-- Manager Profile
INSERT INTO UserProfiles (full_name, phone_number, email, address, id_card_number, date_of_birth, gender)
VALUES 
('Trần Thị Manager', '0901234568', 'manager@diamond.com', '456 Đường XYZ, Quận 3, TP.HCM', '123456789013', '1985-05-15', 'Nữ');

-- Consulting Staff Profiles
INSERT INTO UserProfiles (full_name, phone_number, email, address, id_card_number, date_of_birth, gender)
VALUES 
('Lê Văn Tư Vấn', '0901234569', 'consultant1@diamond.com', '789 Đường DEF, Quận 5, TP.HCM', '123456789014', '1990-03-20', 'Nam'),
('Phạm Thị Tư Vấn', '0901234570', 'consultant2@diamond.com', '321 Đường GHI, Quận 7, TP.HCM', '123456789015', '1992-07-10', 'Nữ');

-- Assessment Staff Profiles
INSERT INTO UserProfiles (full_name, phone_number, email, address, id_card_number, date_of_birth, gender)
VALUES 
('Hoàng Văn Giám Định', '0901234571', 'assessor1@diamond.com', '654 Đường JKL, Quận 10, TP.HCM', '123456789016', '1988-11-25', 'Nam'),
('Võ Thị Giám Định', '0901234572', 'assessor2@diamond.com', '987 Đường MNO, Quận 11, TP.HCM', '123456789017', '1991-09-05', 'Nữ');

-- Customer Profiles
INSERT INTO UserProfiles (full_name, phone_number, email, address, id_card_number, date_of_birth, gender)
VALUES 
('Nguyễn Thị Khách Hàng', '0901234573', 'customer1@email.com', '147 Đường PQR, Quận 2, TP.HCM', '123456789018', '1995-12-30', 'Nữ'),
('Trần Văn Khách Hàng', '0901234574', 'customer2@email.com', '258 Đường STU, Quận 4, TP.HCM', '123456789019', '1987-04-18', 'Nam'),
('Lê Thị Khách Hàng', '0901234575', 'customer3@email.com', '369 Đường VWX, Quận 6, TP.HCM', '123456789020', '1993-08-22', 'Nữ');

GO

-- =====================================================
-- 2. INSERT USERS (Tài khoản người dùng)
-- =====================================================

-- Admin User
INSERT INTO Users (username, password_hash, email, profile_id, role_id)
VALUES ('admin', 'hashed_password_123', 'admin@diamond.com', 1, 1);

-- Manager User
INSERT INTO Users (username, password_hash, email, profile_id, role_id)
VALUES ('manager', 'hashed_password_456', 'manager@diamond.com', 2, 2);

-- Consulting Staff Users
INSERT INTO Users (username, password_hash, email, profile_id, role_id)
VALUES 
('consultant1', 'hashed_password_789', 'consultant1@diamond.com', 3, 3),
('consultant2', 'hashed_password_101', 'consultant2@diamond.com', 4, 3);

-- Assessment Staff Users
INSERT INTO Users (username, password_hash, email, profile_id, role_id)
VALUES 
('assessor1', 'hashed_password_112', 'assessor1@diamond.com', 5, 4),
('assessor2', 'hashed_password_131', 'assessor2@diamond.com', 6, 4);

-- Customer Users
INSERT INTO Users (username, password_hash, email, profile_id, role_id)
VALUES 
('customer1', 'hashed_password_415', 'customer1@email.com', 7, 5),
('customer2', 'hashed_password_161', 'customer2@email.com', 8, 5),
('customer3', 'hashed_password_718', 'customer3@email.com', 9, 5);

GO

-- =====================================================
-- 3. INSERT ASSESSMENT REQUESTS (Phiếu yêu cầu giám định)
-- =====================================================

INSERT INTO AssessmentRequests (customer_id, service_id, request_date, status, customer_notes)
VALUES 
(7, 1, DATEADD(day, -10, GETDATE()), 'Completed', 'Cần giám định kim cương nhẫn cưới'),
(8, 2, DATEADD(day, -7, GETDATE()), 'In Progress', 'Giám định kim cương thô'),
(9, 3, DATEADD(day, -5, GETDATE()), 'Pending', 'Giám định kim cương cao cấp cho bảo hiểm'),
(7, 1, DATEADD(day, -3, GETDATE()), 'Pending', 'Giám định kim cương trang sức'),
(8, 2, DATEADD(day, -1, GETDATE()), 'Pending', 'Giám định kim cương đầu tư');

GO

-- =====================================================
-- 4. INSERT ASSESSMENT RECEIPTS (Biên nhận giám định)
-- =====================================================

INSERT INTO AssessmentReceipts (request_id, consultant_staff_id, receive_date, sample_description, sample_condition)
VALUES 
(1, 3, DATEADD(day, -9, GETDATE()), 'Kim cương tròn 1.5 carat, màu D, độ tinh khiết VVS1', 'Tốt'),
(2, 4, DATEADD(day, -6, GETDATE()), 'Kim cương thô 3.2 carat, màu vàng nhạt', 'Cần làm sạch'),
(3, 3, DATEADD(day, -4, GETDATE()), 'Kim cương princess cut 2.1 carat, màu F, độ tinh khiết VS1', 'Tốt');

GO

-- =====================================================
-- 5. INSERT ASSESSMENT RESULTS (Kết quả giám định)
-- =====================================================

INSERT INTO AssessmentResults (
    receipt_id, assessor_id, result_date, 
    diamond_origin, shape_and_cut, measurements, carat_weight, 
    color, clarity, cut, polish, symmetry, fluorescence,
    comments, assessment_notes
)
VALUES 
(1, 5, DATEADD(day, -8, GETDATE()), 
 'Natural', 'Round Brilliant', '6.5 x 6.5 x 4.0 mm', 1.52, 
 'D', 'VVS1', 'Excellent', 'Excellent', 'Excellent', 'None',
 'Kim cương chất lượng cao, phù hợp cho nhẫn cưới', 'Đã kiểm tra bằng máy móc hiện đại'),

(2, 6, DATEADD(day, -5, GETDATE()), 
 'Natural', 'Rough', '8.2 x 7.1 x 5.3 mm', 3.18, 
 'K', 'SI2', 'N/A', 'N/A', 'N/A', 'Medium Blue',
 'Kim cương thô, cần gia công thêm', 'Đã làm sạch và phân tích cấu trúc'),

(3, 5, DATEADD(day, -3, GETDATE()), 
 'Natural', 'Princess Cut', '7.8 x 7.8 x 5.2 mm', 2.08, 
 'F', 'VS1', 'Very Good', 'Excellent', 'Very Good', 'None',
 'Kim cương princess cut đẹp, phù hợp cho trang sức cao cấp', 'Đã kiểm tra tỷ lệ cắt mài');

GO

-- =====================================================
-- 6. INSERT CERTIFICATES (Giấy giám định)
-- =====================================================

INSERT INTO Certificates (assessment_id, certificate_code, issue_date, price, certificate_type, is_digital)
VALUES 
(1, 'CERT-2024-001', DATEADD(day, -7, GETDATE()), 500000, 'Basic Certificate', 1),
(2, 'CERT-2024-002', DATEADD(day, -4, GETDATE()), 800000, 'Advanced Certificate', 1),
(3, 'CERT-2024-003', DATEADD(day, -2, GETDATE()), 1200000, 'Premium Certificate', 1);

GO

-- =====================================================
-- 7. INSERT MANAGER APPROVALS (Phê duyệt quản lý)
-- =====================================================

INSERT INTO ManagerApprovals (request_id, manager_id, approval_date, status, comments, approval_type)
VALUES 
(1, 2, DATEADD(day, -9, GETDATE()), 'Approved', 'Đồng ý giám định kim cương nhẫn cưới', 'Assessment'),
(2, 2, DATEADD(day, -6, GETDATE()), 'Approved', 'Đồng ý giám định kim cương thô', 'Assessment'),
(3, 2, DATEADD(day, -4, GETDATE()), 'Approved', 'Đồng ý giám định kim cương cao cấp', 'Assessment');

GO

-- =====================================================
-- 8. INSERT CUSTOMER CONTACTS (Lịch sử liên hệ)
-- =====================================================

INSERT INTO CustomerContacts (customer_id, staff_id, contact_date, contact_type, contact_method, contact_summary, follow_up_required, status)
VALUES 
(7, 3, DATEADD(day, -11, GETDATE()), 'Phone', '0901234569', 'Khách hàng hỏi về dịch vụ giám định kim cương', 0, 'Completed'),
(8, 4, DATEADD(day, -8, GETDATE()), 'Email', 'customer2@email.com', 'Gửi thông tin dịch vụ và bảng giá', 1, 'Completed'),
(9, 3, DATEADD(day, -6, GETDATE()), 'In-person', 'Văn phòng', 'Khách hàng đến tư vấn trực tiếp', 0, 'Completed'),
(7, 4, DATEADD(day, -4, GETDATE()), 'SMS', '0901234573', 'Nhắc nhở khách hàng về lịch hẹn', 0, 'Completed');

GO

-- =====================================================
-- 9. INSERT SAMPLE TRACKING (Theo dõi mẫu)
-- =====================================================

INSERT INTO SampleTracking (receipt_id, location, status, moved_by, notes)
VALUES 
(1, 'Storage', 'Received', 3, 'Đã nhận mẫu từ khách hàng'),
(1, 'Assessment Lab', 'In Assessment', 5, 'Chuyển đến phòng giám định'),
(1, 'Sealing Room', 'Sealed', 5, 'Đã niêm phong sau giám định'),
(1, 'Storage', 'Delivered', 3, 'Đã trả cho khách hàng'),

(2, 'Storage', 'Received', 4, 'Đã nhận mẫu từ khách hàng'),
(2, 'Assessment Lab', 'In Assessment', 6, 'Đang trong quá trình giám định'),

(3, 'Storage', 'Received', 3, 'Đã nhận mẫu từ khách hàng'),
(3, 'Assessment Lab', 'In Assessment', 5, 'Đang trong quá trình giám định');

GO

-- =====================================================
-- 10. INSERT SEALING RECORDS (Biên bản niêm phong)
-- =====================================================

INSERT INTO SealingRecords (assessment_id, sealed_by, sealed_at, sealing_method, sealing_notes, seal_number)
VALUES 
(1, 5, DATEADD(day, -7, GETDATE()), 'Laser Sealing', 'Niêm phong bằng laser, đảm bảo an toàn', 'SEAL-2024-001'),
(2, 6, DATEADD(day, -4, GETDATE()), 'Manual Sealing', 'Niêm phong thủ công do kích thước lớn', 'SEAL-2024-002'),
(3, 5, DATEADD(day, -2, GETDATE()), 'Laser Sealing', 'Niêm phong bằng laser', 'SEAL-2024-003');

GO

-- =====================================================
-- 11. INSERT PAYMENTS (Thanh toán)
-- =====================================================

INSERT INTO Payments (request_id, amount, payment_method, payment_date, payment_status, transaction_id, receipt_number, notes)
VALUES 
(1, 500000, 'Cash', DATEADD(day, -9, GETDATE()), 'Completed', 'TXN-2024-001', 'RCPT-2024-001', 'Thanh toán tiền mặt'),
(2, 800000, 'Bank Transfer', DATEADD(day, -6, GETDATE()), 'Completed', 'TXN-2024-002', 'RCPT-2024-002', 'Chuyển khoản ngân hàng'),
(3, 1200000, 'Credit Card', DATEADD(day, -4, GETDATE()), 'Completed', 'TXN-2024-003', 'RCPT-2024-003', 'Thanh toán bằng thẻ tín dụng');

GO

-- =====================================================
-- CẬP NHẬT TRẠNG THÁI ASSESSMENT REQUESTS
-- =====================================================

-- Cập nhật trạng thái cho các request đã hoàn thành
UPDATE AssessmentRequests 
SET status = 'Completed' 
WHERE request_id IN (1, 2, 3);

GO

PRINT 'Đã insert thành công dữ liệu mẫu cho DiamondDB!';
PRINT '';
PRINT 'Dữ liệu đã được thêm:';
PRINT '- 9 UserProfiles (Admin, Manager, Staff, Customers)';
PRINT '- 9 Users với các vai trò khác nhau';
PRINT '- 5 AssessmentRequests với các trạng thái khác nhau';
PRINT '- 3 AssessmentReceipts';
PRINT '- 3 AssessmentResults với thông số kim cương chi tiết';
PRINT '- 3 Certificates';
PRINT '- 3 ManagerApprovals';
PRINT '- 4 CustomerContacts';
PRINT '- 8 SampleTracking records';
PRINT '- 3 SealingRecords';
PRINT '- 3 Payments';
PRINT '';
PRINT 'Bạn có thể sử dụng các Views sau để xem dữ liệu:';
PRINT '- vw_AssessmentRequestDetails: Xem chi tiết assessment requests';
PRINT '- vw_DashboardStats: Xem thống kê dashboard';
