-- =====================================================
-- INSERT SAMPLE DATA FOR DIAMOND ASSESSMENT SYSTEM
-- Database: DiamondDB
-- Encoding: UTF-8 with N prefix for Vietnamese text
-- =====================================================

USE DiamondDB;
GO

-- =====================================================
-- 1. INSERT USER PROFILES (Thong tin ca nhan)
-- =====================================================

-- Admin Profile
INSERT INTO UserProfiles (full_name, phone_number, email, address, id_card_number, date_of_birth, gender)
VALUES 
(N'Nguyen Van Admin', '0901234567', 'admin@diamond.com', N'123 Duong ABC, Quan 1, TP.HCM', '123456789012', '1980-01-01', N'Nam');

-- Manager Profile
INSERT INTO UserProfiles (full_name, phone_number, email, address, id_card_number, date_of_birth, gender)
VALUES 
(N'Tran Thi Manager', '0901234568', 'manager@diamond.com', N'456 Duong XYZ, Quan 3, TP.HCM', '123456789013', '1985-05-15', N'Nu');

-- Consulting Staff Profiles
INSERT INTO UserProfiles (full_name, phone_number, email, address, id_card_number, date_of_birth, gender)
VALUES 
(N'Le Van Tu Van', '0901234569', 'consultant1@diamond.com', N'789 Duong DEF, Quan 5, TP.HCM', '123456789014', '1990-03-20', N'Nam'),
(N'Pham Thi Tu Van', '0901234570', 'consultant2@diamond.com', N'321 Duong GHI, Quan 7, TP.HCM', '123456789015', '1992-07-10', N'Nu');

-- Assessment Staff Profiles
INSERT INTO UserProfiles (full_name, phone_number, email, address, id_card_number, date_of_birth, gender)
VALUES 
(N'Hoang Van Giam Dinh', '0901234571', 'assessor1@diamond.com', N'654 Duong JKL, Quan 10, TP.HCM', '123456789016', '1988-11-25', N'Nam'),
(N'Vo Thi Giam Dinh', '0901234572', 'assessor2@diamond.com', N'987 Duong MNO, Quan 11, TP.HCM', '123456789017', '1991-09-05', N'Nu');

-- Customer Profiles
INSERT INTO UserProfiles (full_name, phone_number, email, address, id_card_number, date_of_birth, gender)
VALUES 
(N'Nguyen Thi Khach Hang', '0901234573', 'customer1@email.com', N'147 Duong PQR, Quan 2, TP.HCM', '123456789018', '1995-12-30', N'Nu'),
(N'Tran Van Khach Hang', '0901234574', 'customer2@email.com', N'258 Duong STU, Quan 4, TP.HCM', '123456789019', '1987-04-18', N'Nam'),
(N'Le Thi Khach Hang', '0901234575', 'customer3@email.com', N'369 Duong VWX, Quan 6, TP.HCM', '123456789020', '1993-08-22', N'Nu');

GO

-- =====================================================
-- 2. INSERT USERS (Tai khoan nguoi dung)
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
-- 3. INSERT ASSESSMENT REQUESTS (Phieu yeu cau giam dinh)
-- =====================================================

INSERT INTO AssessmentRequests (customer_id, service_id, request_date, status, customer_notes)
VALUES 
(7, 1, DATEADD(day, -10, GETDATE()), 'Completed', N'Can giam dinh kim cuong nhan cuoi'),
(8, 2, DATEADD(day, -7, GETDATE()), 'In Progress', N'Giam dinh kim cuong tho'),
(9, 3, DATEADD(day, -5, GETDATE()), 'Pending', N'Giam dinh kim cuong cao cap cho bao hiem'),
(7, 1, DATEADD(day, -3, GETDATE()), 'Pending', N'Giam dinh kim cuong trang suc'),
(8, 2, DATEADD(day, -1, GETDATE()), 'Pending', N'Giam dinh kim cuong dau tu');

GO

-- =====================================================
-- 4. INSERT ASSESSMENT RECEIPTS (Bien nhan giam dinh)
-- =====================================================

INSERT INTO AssessmentReceipts (request_id, consultant_staff_id, receive_date, sample_description, sample_condition)
VALUES 
(1, 3, DATEADD(day, -9, GETDATE()), N'Kim cuong tron 1.5 carat, mau D, do tinh khiet VVS1', N'Tot'),
(2, 4, DATEADD(day, -6, GETDATE()), N'Kim cuong tho 3.2 carat, mau vang nhat', N'Can lam sach'),
(3, 3, DATEADD(day, -4, GETDATE()), N'Kim cuong princess cut 2.1 carat, mau F, do tinh khiet VS1', N'Tot');

GO

-- =====================================================
-- 5. INSERT ASSESSMENT RESULTS (Ket qua giam dinh)
-- =====================================================

INSERT INTO AssessmentResults (receipt_id, assessor_id, result_date, diamond_origin, shape_and_cut, measurements, carat_weight, color, clarity, cut, polish, symmetry, fluorescence, comments)
VALUES 
(1, 5, DATEADD(day, -7, GETDATE()), N'Thien nhien', N'Round Brilliant', '6.5 x 6.5 x 4.0 mm', 1.52, 'D', 'VVS1', 'Excellent', 'Excellent', 'Excellent', N'Khong', N'Kim cuong chat luong cao'),
(2, 6, DATEADD(day, -4, GETDATE()), N'Thien nhien', N'Rough', '8.2 x 7.1 x 5.3 mm', 3.18, 'K', 'SI2', 'Fair', 'Good', 'Good', N'Vang nhat', N'Kim cuong tho can xu ly them'),
(3, 5, DATEADD(day, -2, GETDATE()), N'Thien nhien', N'Princess Cut', '7.8 x 7.8 x 5.9 mm', 2.08, 'F', 'VS1', 'Very Good', 'Very Good', 'Very Good', N'Khong', N'Kim cuong princess cut dep');

GO

-- =====================================================
-- 6. INSERT CERTIFICATES (Giay giam dinh)
-- =====================================================

INSERT INTO Certificates (assessment_id, certificate_code, issue_date, price, certificate_type)
VALUES 
(1, 'CERT-2024-001', DATEADD(day, -6, GETDATE()), 500000, N'Chung chi co ban'),
(2, 'CERT-2024-002', DATEADD(day, -3, GETDATE()), 800000, N'Chung chi nang cao'),
(3, 'CERT-2024-003', DATEADD(day, -1, GETDATE()), 1200000, N'Chung chi quoc te');

GO

-- =====================================================
-- 7. INSERT MANAGER APPROVALS (Phe duyet quan ly)
-- =====================================================

INSERT INTO ManagerApprovals (request_id, manager_id, approval_date, status, comments, approval_type)
VALUES 
(1, 2, DATEADD(day, -8, GETDATE()), 'Approved', N'Phe duyet giam dinh kim cuong nhan cuoi', 'Assessment'),
(2, 2, DATEADD(day, -5, GETDATE()), 'Approved', N'Phe duyet giam dinh kim cuong tho', 'Assessment'),
(3, 2, DATEADD(day, -3, GETDATE()), 'Approved', N'Phe duyet giam dinh kim cuong cao cap', 'Assessment');

GO

-- =====================================================
-- 8. INSERT CUSTOMER CONTACTS (Lich su lien he)
-- =====================================================

INSERT INTO CustomerContacts (customer_id, staff_id, contact_date, contact_type, contact_method, contact_summary, status)
VALUES 
(7, 3, DATEADD(day, -11, GETDATE()), 'Phone', N'Goi dien', N'Tu van ve dich vu giam dinh kim cuong', 'Completed'),
(8, 4, DATEADD(day, -8, GETDATE()), 'Email', N'Email', N'Gui thong tin dich vu va bang gia', 'Completed'),
(9, 3, DATEADD(day, -6, GETDATE()), 'In-person', N'Truc tiep', N'Gap mat tu van va ky hop dong', 'Completed');

GO

-- =====================================================
-- 9. INSERT SAMPLE TRACKING (Theo doi mau)
-- =====================================================

INSERT INTO SampleTracking (receipt_id, location, status, moved_by, notes)
VALUES 
(1, N'Kho luu tru', 'Received', 3, N'Nhan mau tu khach hang'),
(1, N'Phong giam dinh', 'In Assessment', 5, N'Chuyen den phong giam dinh'),
(1, N'Phong niem phong', 'Sealed', 6, N'Niem phong sau khi giam dinh'),
(2, N'Kho luu tru', 'Received', 4, N'Nhan mau kim cuong tho'),
(2, N'Phong giam dinh', 'In Assessment', 6, N'Dang trong qua trinh giam dinh');

GO

-- =====================================================
-- 10. INSERT SEALING RECORDS (Bien ban niem phong)
-- =====================================================

INSERT INTO SealingRecords (assessment_id, sealed_by, sealed_at, sealing_method, sealing_notes, seal_number)
VALUES 
(1, 6, DATEADD(day, -6, GETDATE()), N'Niem phong bang keo', N'Niem phong kim cuong vao vi', 'SEAL-2024-001'),
(3, 5, DATEADD(day, -1, GETDATE()), N'Niem phong bang keo', N'Niem phong kim cuong princess cut', 'SEAL-2024-002');

GO

-- =====================================================
-- 11. INSERT PAYMENTS (Thanh toan)
-- =====================================================

INSERT INTO Payments (request_id, amount, payment_method, payment_date, payment_status, transaction_id, receipt_number)
VALUES 
(1, 500000, N'Tien mat', DATEADD(day, -9, GETDATE()), 'Completed', 'TXN-001', 'RCP-001'),
(2, 800000, N'Chuyen khoan', DATEADD(day, -6, GETDATE()), 'Completed', 'TXN-002', 'RCP-002'),
(3, 1200000, N'The tin dung', DATEADD(day, -4, GETDATE()), 'Completed', 'TXN-003', 'RCP-003'),
(4, 500000, N'Tien mat', DATEADD(day, -2, GETDATE()), 'Pending', 'TXN-004', 'RCP-004'),
(5, 800000, N'Chuyen khoan', DATEADD(day, -1, GETDATE()), 'Pending', 'TXN-005', 'RCP-005');

GO

-- =====================================================
-- UPDATE STATUS FOR SOME ASSESSMENT REQUESTS
-- =====================================================

UPDATE AssessmentRequests 
SET status = 'In Progress' 
WHERE request_id IN (4, 5);

GO

PRINT N'Da them thanh cong du lieu mau!';
PRINT N'Cac bang da duoc them du lieu:';
PRINT N'- UserProfiles: 9 ban ghi';
PRINT N'- Users: 9 tai khoan';
PRINT N'- AssessmentRequests: 5 yeu cau';
PRINT N'- AssessmentReceipts: 3 bien nhan';
PRINT N'- AssessmentResults: 3 ket qua';
PRINT N'- Certificates: 3 chung chi';
PRINT N'- ManagerApprovals: 3 phe duyet';
PRINT N'- CustomerContacts: 3 lien he';
PRINT N'- SampleTracking: 5 theo doi';
PRINT N'- SealingRecords: 2 niem phong';
PRINT N'- Payments: 5 thanh toan';
