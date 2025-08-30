-- =====================================================
-- Diamond Assessment System Database Schema
-- Database: DiamondDB
-- Description: Hệ thống quản lý giám định kim cương
-- =====================================================

-- Tạo database
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'DiamondDB')
BEGIN
    CREATE DATABASE DiamondDB;
END
GO

USE DiamondDB;
GO

-- =====================================================
-- 1. BẢNG ROLES (Vai trò người dùng)
-- =====================================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Roles')
BEGIN
    CREATE TABLE Roles (
        role_id INT IDENTITY(1,1) PRIMARY KEY,
        role_name NVARCHAR(100) NOT NULL UNIQUE,
        description NVARCHAR(500),
        is_active BIT DEFAULT 1,
        created_at DATETIME DEFAULT GETDATE(),
        updated_at DATETIME DEFAULT GETDATE()
    );
END
GO

-- =====================================================
-- 2. BẢNG USER PROFILES (Thông tin cá nhân)
-- =====================================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'UserProfiles')
BEGIN
    CREATE TABLE UserProfiles (
        profile_id INT IDENTITY(1,1) PRIMARY KEY,
        full_name NVARCHAR(255) NOT NULL,
        phone_number NVARCHAR(20),
        email NVARCHAR(255),
        address NVARCHAR(500),
        id_card_number NVARCHAR(20),
        date_of_birth DATE,
        gender NVARCHAR(10),
        is_active BIT DEFAULT 1,
        created_at DATETIME DEFAULT GETDATE(),
        updated_at DATETIME DEFAULT GETDATE()
    );
END
GO

-- =====================================================
-- 3. BẢNG USERS (Tài khoản người dùng)
-- =====================================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Users')
BEGIN
    CREATE TABLE Users (
        user_id INT IDENTITY(1,1) PRIMARY KEY,
        username NVARCHAR(100) NOT NULL UNIQUE,
        password_hash NVARCHAR(255) NOT NULL,
        email NVARCHAR(255) UNIQUE,
        profile_id INT NOT NULL,
        role_id INT NOT NULL,
        is_active BIT DEFAULT 1,
        last_login DATETIME,
        created_at DATETIME DEFAULT GETDATE(),
        updated_at DATETIME DEFAULT GETDATE(),
        
        CONSTRAINT FK_Users_UserProfiles FOREIGN KEY (profile_id) REFERENCES UserProfiles(profile_id),
        CONSTRAINT FK_Users_Roles FOREIGN KEY (role_id) REFERENCES Roles(role_id)
    );
END
GO

-- =====================================================
-- 4. BẢNG SERVICES (Dịch vụ giám định)
-- =====================================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Services')
BEGIN
    CREATE TABLE Services (
        service_id INT IDENTITY(1,1) PRIMARY KEY,
        service_name NVARCHAR(255) NOT NULL,
        description NVARCHAR(1000),
        price DECIMAL(10,2) NOT NULL,
        estimated_duration_days INT NOT NULL,
        is_active BIT DEFAULT 1,
        created_at DATETIME DEFAULT GETDATE(),
        updated_at DATETIME DEFAULT GETDATE()
    );
END
GO

-- =====================================================
-- 5. BẢNG ASSESSMENT REQUESTS (Phiếu yêu cầu giám định)
-- =====================================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'AssessmentRequests')
BEGIN
    CREATE TABLE AssessmentRequests (
        request_id INT IDENTITY(1,1) PRIMARY KEY,
        customer_id INT NOT NULL,
        service_id INT NOT NULL,
        request_date DATETIME DEFAULT GETDATE(),
        status NVARCHAR(50) DEFAULT 'Pending',
        customer_notes NVARCHAR(1000),
        created_at DATETIME DEFAULT GETDATE(),
        updated_at DATETIME DEFAULT GETDATE(),
        
        CONSTRAINT FK_AssessmentRequests_Users FOREIGN KEY (customer_id) REFERENCES Users(user_id),
        CONSTRAINT FK_AssessmentRequests_Services FOREIGN KEY (service_id) REFERENCES Services(service_id)
    );
END
GO

-- =====================================================
-- 6. BẢNG ASSESSMENT RECEIPTS (Biên nhận giám định)
-- =====================================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'AssessmentReceipts')
BEGIN
    CREATE TABLE AssessmentReceipts (
        receipt_id INT IDENTITY(1,1) PRIMARY KEY,
        request_id INT NOT NULL UNIQUE,
        consultant_staff_id INT NOT NULL,
        receive_date DATETIME DEFAULT GETDATE(),
        sample_description NVARCHAR(1000),
        sample_condition NVARCHAR(500),
        customer_signature NVARCHAR(255),
        consultant_signature NVARCHAR(255),
        created_at DATETIME DEFAULT GETDATE(),
        updated_at DATETIME DEFAULT GETDATE(),
        
        CONSTRAINT FK_AssessmentReceipts_AssessmentRequests FOREIGN KEY (request_id) REFERENCES AssessmentRequests(request_id),
        CONSTRAINT FK_AssessmentReceipts_Users FOREIGN KEY (consultant_staff_id) REFERENCES Users(user_id)
    );
END
GO

-- =====================================================
-- 7. BẢNG ASSESSMENT RESULTS (Kết quả giám định)
-- =====================================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'AssessmentResults')
BEGIN
    CREATE TABLE AssessmentResults (
        assessment_id INT IDENTITY(1,1) PRIMARY KEY,
        receipt_id INT NOT NULL UNIQUE,
        assessor_id INT NOT NULL,
        result_date DATETIME DEFAULT GETDATE(),
        
        -- Thông số kim cương
        diamond_origin NVARCHAR(100),
        shape_and_cut NVARCHAR(100),
        measurements NVARCHAR(100),
        carat_weight DECIMAL(10,2) NOT NULL,
        color NVARCHAR(50),
        clarity NVARCHAR(50),
        cut NVARCHAR(50),
        polish NVARCHAR(50),
        symmetry NVARCHAR(50),
        fluorescence NVARCHAR(50),
        
        -- Thông tin bổ sung
        comments NVARCHAR(1000),
        assessment_notes NVARCHAR(1000),
        created_at DATETIME DEFAULT GETDATE(),
        updated_at DATETIME DEFAULT GETDATE(),
        
        CONSTRAINT FK_AssessmentResults_AssessmentReceipts FOREIGN KEY (receipt_id) REFERENCES AssessmentReceipts(receipt_id),
        CONSTRAINT FK_AssessmentResults_Users FOREIGN KEY (assessor_id) REFERENCES Users(user_id)
    );
END
GO

-- =====================================================
-- 8. BẢNG CERTIFICATES (Giấy giám định)
-- =====================================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Certificates')
BEGIN
    CREATE TABLE Certificates (
        certificate_id INT IDENTITY(1,1) PRIMARY KEY,
        assessment_id INT NOT NULL UNIQUE,
        certificate_code NVARCHAR(100) NOT NULL UNIQUE,
        issue_date DATETIME DEFAULT GETDATE(),
        price DECIMAL(10,2) NOT NULL,
        certificate_type NVARCHAR(100),
        is_digital BIT DEFAULT 0,
        digital_certificate_url NVARCHAR(500),
        created_at DATETIME DEFAULT GETDATE(),
        updated_at DATETIME DEFAULT GETDATE(),
        
        CONSTRAINT FK_Certificates_AssessmentResults FOREIGN KEY (assessment_id) REFERENCES AssessmentResults(assessment_id)
    );
END
GO

-- =====================================================
-- 9. BẢNG MANAGER APPROVALS (Phê duyệt quản lý)
-- =====================================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'ManagerApprovals')
BEGIN
    CREATE TABLE ManagerApprovals (
        approval_id INT IDENTITY(1,1) PRIMARY KEY,
        request_id INT NOT NULL,
        manager_id INT NOT NULL,
        approval_date DATETIME DEFAULT GETDATE(),
        status NVARCHAR(50) NOT NULL, -- 'Approved', 'Rejected', 'Pending'
        comments NVARCHAR(1000),
        approval_type NVARCHAR(100), -- 'Assessment', 'Certificate', 'Refund', etc.
        created_at DATETIME DEFAULT GETDATE(),
        updated_at DATETIME DEFAULT GETDATE(),
        
        CONSTRAINT FK_ManagerApprovals_AssessmentRequests FOREIGN KEY (request_id) REFERENCES AssessmentRequests(request_id),
        CONSTRAINT FK_ManagerApprovals_Users FOREIGN KEY (manager_id) REFERENCES Users(user_id)
    );
END
GO

-- =====================================================
-- 10. BẢNG CUSTOMER CONTACTS (Lịch sử liên hệ khách hàng)
-- =====================================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'CustomerContacts')
BEGIN
    CREATE TABLE CustomerContacts (
        contact_id INT IDENTITY(1,1) PRIMARY KEY,
        customer_id INT NOT NULL,
        staff_id INT NOT NULL,
        contact_date DATETIME DEFAULT GETDATE(),
        contact_type NVARCHAR(50), -- 'Phone', 'Email', 'SMS', 'In-person'
        contact_method NVARCHAR(100),
        contact_summary NVARCHAR(1000),
        follow_up_required BIT DEFAULT 0,
        follow_up_date DATETIME,
        status NVARCHAR(50), -- 'Completed', 'Pending', 'No Answer'
        created_at DATETIME DEFAULT GETDATE(),
        updated_at DATETIME DEFAULT GETDATE(),
        
        CONSTRAINT FK_CustomerContacts_Customer FOREIGN KEY (customer_id) REFERENCES Users(user_id),
        CONSTRAINT FK_CustomerContacts_Staff FOREIGN KEY (staff_id) REFERENCES Users(user_id)
    );
END
GO

-- =====================================================
-- 11. BẢNG SAMPLE TRACKING (Theo dõi mẫu)
-- =====================================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'SampleTracking')
BEGIN
    CREATE TABLE SampleTracking (
        tracking_id INT IDENTITY(1,1) PRIMARY KEY,
        receipt_id INT NOT NULL,
        location NVARCHAR(100), -- 'Storage', 'Assessment Lab', 'Sealing Room', 'Delivery'
        status NVARCHAR(50), -- 'Received', 'In Assessment', 'Sealed', 'Delivered'
        moved_by INT NOT NULL,
        moved_at DATETIME DEFAULT GETDATE(),
        notes NVARCHAR(500),
        created_at DATETIME DEFAULT GETDATE(),
        
        CONSTRAINT FK_SampleTracking_AssessmentReceipts FOREIGN KEY (receipt_id) REFERENCES AssessmentReceipts(receipt_id),
        CONSTRAINT FK_SampleTracking_Users FOREIGN KEY (moved_by) REFERENCES Users(user_id)
    );
END
GO

-- =====================================================
-- 12. BẢNG SEALING RECORDS (Biên bản niêm phong)
-- =====================================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'SealingRecords')
BEGIN
    CREATE TABLE SealingRecords (
        sealing_id INT IDENTITY(1,1) PRIMARY KEY,
        assessment_id INT NOT NULL,
        sealed_by INT NOT NULL,
        sealed_at DATETIME DEFAULT GETDATE(),
        sealing_method NVARCHAR(100),
        sealing_notes NVARCHAR(1000),
        seal_number NVARCHAR(100),
        is_active BIT DEFAULT 1,
        created_at DATETIME DEFAULT GETDATE(),
        updated_at DATETIME DEFAULT GETDATE(),
        
        CONSTRAINT FK_SealingRecords_AssessmentResults FOREIGN KEY (assessment_id) REFERENCES AssessmentResults(assessment_id),
        CONSTRAINT FK_SealingRecords_Users FOREIGN KEY (sealed_by) REFERENCES Users(user_id)
    );
END
GO

-- =====================================================
-- 13. BẢNG PAYMENTS (Thanh toán)
-- =====================================================
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Payments')
BEGIN
    CREATE TABLE Payments (
        payment_id INT IDENTITY(1,1) PRIMARY KEY,
        request_id INT NOT NULL,
        amount DECIMAL(10,2) NOT NULL,
        payment_method NVARCHAR(50), -- 'Cash', 'Bank Transfer', 'Credit Card'
        payment_date DATETIME DEFAULT GETDATE(),
        payment_status NVARCHAR(50) DEFAULT 'Pending', -- 'Pending', 'Completed', 'Failed'
        transaction_id NVARCHAR(100),
        receipt_number NVARCHAR(100),
        notes NVARCHAR(500),
        created_at DATETIME DEFAULT GETDATE(),
        updated_at DATETIME DEFAULT GETDATE(),
        
        CONSTRAINT FK_Payments_AssessmentRequests FOREIGN KEY (request_id) REFERENCES AssessmentRequests(request_id)
    );
END
GO

-- =====================================================
-- INSERT DỮ LIỆU MẪU
-- =====================================================

-- Insert Roles
IF NOT EXISTS (SELECT * FROM Roles WHERE role_name = 'Admin')
BEGIN
    INSERT INTO Roles (role_name, description) VALUES 
    ('Admin', 'Quản trị viên hệ thống'),
    ('Manager', 'Quản lý'),
    ('Consulting Staff', 'Nhân viên tư vấn'),
    ('Assessment Staff', 'Nhân viên giám định'),
    ('Customer', 'Khách hàng'),
    ('Guest', 'Khách vãng lai');
END
GO

-- Insert Services
IF NOT EXISTS (SELECT * FROM Services WHERE service_name = 'Giám định kim cương cơ bản')
BEGIN
    INSERT INTO Services (service_name, description, price, estimated_duration_days) VALUES 
    ('Giám định kim cương cơ bản', 'Giám định các thông số cơ bản của kim cương', 500000, 3),
    ('Giám định kim cương nâng cao', 'Giám định chi tiết với báo cáo đầy đủ', 800000, 5),
    ('Giám định kim cương cao cấp', 'Giám định với chứng chỉ quốc tế', 1200000, 7);
END
GO

-- =====================================================
-- TẠO INDEXES ĐỂ TỐI ƯU HIỆU SUẤT
-- =====================================================

-- Indexes cho Users
CREATE INDEX IX_Users_Username ON Users(username);
CREATE INDEX IX_Users_Email ON Users(email);
CREATE INDEX IX_Users_RoleId ON Users(role_id);

-- Indexes cho AssessmentRequests
CREATE INDEX IX_AssessmentRequests_CustomerId ON AssessmentRequests(customer_id);
CREATE INDEX IX_AssessmentRequests_Status ON AssessmentRequests(status);
CREATE INDEX IX_AssessmentRequests_RequestDate ON AssessmentRequests(request_date);

-- Indexes cho AssessmentResults
CREATE INDEX IX_AssessmentResults_AssessorId ON AssessmentResults(assessor_id);
CREATE INDEX IX_AssessmentResults_ResultDate ON AssessmentResults(result_date);

-- Indexes cho Certificates
CREATE INDEX IX_Certificates_CertificateCode ON Certificates(certificate_code);
CREATE INDEX IX_Certificates_IssueDate ON Certificates(issue_date);

-- Indexes cho CustomerContacts
CREATE INDEX IX_CustomerContacts_CustomerId ON CustomerContacts(customer_id);
CREATE INDEX IX_CustomerContacts_ContactDate ON CustomerContacts(contact_date);

-- Indexes cho Payments
CREATE INDEX IX_Payments_RequestId ON Payments(request_id);
CREATE INDEX IX_Payments_PaymentStatus ON Payments(payment_status);

GO

-- =====================================================
-- TẠO VIEWS HỮU ÍCH
-- =====================================================

-- View: Thông tin đầy đủ của assessment request
CREATE OR ALTER VIEW vw_AssessmentRequestDetails AS
SELECT 
    ar.request_id,
    ar.request_date,
    ar.status as request_status,
    ar.customer_notes,
    
    -- Customer info
    c.full_name as customer_name,
    c.phone_number as customer_phone,
    c.email as customer_email,
    
    -- Service info
    s.service_name,
    s.price as service_price,
    s.estimated_duration_days,
    
    -- Receipt info
    rec.receive_date,
    rec.sample_description,
    
    -- Result info
    res.result_date,
    res.carat_weight,
    res.color,
    res.clarity,
    
    -- Certificate info
    cert.certificate_code,
    cert.issue_date,
    cert.price as certificate_price
    
FROM AssessmentRequests ar
LEFT JOIN Users u ON ar.customer_id = u.user_id
LEFT JOIN UserProfiles c ON u.profile_id = c.profile_id
LEFT JOIN Services s ON ar.service_id = s.service_id
LEFT JOIN AssessmentReceipts rec ON ar.request_id = rec.request_id
LEFT JOIN AssessmentResults res ON rec.receipt_id = res.receipt_id
LEFT JOIN Certificates cert ON res.assessment_id = cert.assessment_id;

GO

-- View: Dashboard statistics
CREATE OR ALTER VIEW vw_DashboardStats AS
SELECT 
    (SELECT COUNT(*) FROM AssessmentRequests WHERE status = 'Pending') as pending_requests,
    (SELECT COUNT(*) FROM AssessmentRequests WHERE status = 'In Progress') as in_progress_requests,
    (SELECT COUNT(*) FROM AssessmentRequests WHERE status = 'Completed') as completed_requests,
    (SELECT COUNT(*) FROM Users WHERE role_id = (SELECT role_id FROM Roles WHERE role_name = 'Customer')) as total_customers,
    (SELECT COUNT(*) FROM Certificates WHERE issue_date >= DATEADD(day, -30, GETDATE())) as certificates_this_month,
    (SELECT SUM(amount) FROM Payments WHERE payment_status = 'Completed' AND payment_date >= DATEADD(day, -30, GETDATE())) as revenue_this_month;

GO

PRINT 'Database DiamondDB đã được tạo thành công!';
PRINT 'Các bảng đã được tạo:';
PRINT '- Roles (Vai trò người dùng)';
PRINT '- UserProfiles (Thông tin cá nhân)';
PRINT '- Users (Tài khoản người dùng)';
PRINT '- Services (Dịch vụ giám định)';
PRINT '- AssessmentRequests (Phiếu yêu cầu giám định)';
PRINT '- AssessmentReceipts (Biên nhận giám định)';
PRINT '- AssessmentResults (Kết quả giám định)';
PRINT '- Certificates (Giấy giám định)';
PRINT '- ManagerApprovals (Phê duyệt quản lý)';
PRINT '- CustomerContacts (Lịch sử liên hệ)';
PRINT '- SampleTracking (Theo dõi mẫu)';
PRINT '- SealingRecords (Biên bản niêm phong)';
PRINT '- Payments (Thanh toán)';
PRINT '';
PRINT 'Dữ liệu mẫu đã được thêm vào bảng Roles và Services';
PRINT 'Indexes và Views đã được tạo để tối ưu hiệu suất';
