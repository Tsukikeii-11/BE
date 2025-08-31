# Flask Clean Architecture - Diamond Assessment System

## Tổng quan dự án
Hệ thống đánh giá kim cương được xây dựng theo mô hình Clean Architecture với Flask, bao gồm các tính năng:
- Quản lý người dùng (User Management)
- Yêu cầu đánh giá (Assessment Request)
- Quá trình đánh giá (Assessment Process)
- Kết quả đánh giá (Assessment Result)
- Phiếu thu (Assessment Receipt)
- Chứng chỉ (Certificate)
- Phê duyệt quản lý (Manager Approval)
- Dịch vụ (Service Management)

## Cấu trúc dự án

```bash
CNPM_C/
├── docs/                        # Documentation
│   └── flask-clean-architecture.md
│
├── instance/                    # Instance configuration
│   └── default.db
├── scripts/                     # Database & utility scripts
│   ├── create_diamond_db.sql    # Database schema creation
│   ├── insert_sample_data.sql   # Sample data insertion
│   ├── insert_sample_data_fixed.sql
│   └── run_postgres.sh          # PostgreSQL runner script
│
├── src/                         # Source code chính
│   ├── api/                     # API Layer (Presentation)
│   │   ├── controllers/         # Request handlers
│   │   │   ├── assessment_receipt_controller.py
│   │   │   ├── assessment_request_controller.py
│   │   │   ├── assessment_result_controller.py
│   │   │   ├── certificate_controller.py
│   │   │   ├── manager_approval_controller.py
│   │   │   ├── service_controller.py
│   │   │   └── user_controller.py
│   │   ├── schemas/             # Data validation & serialization
│   │   │   ├── service_schema.py
│   │   │   └── user_schema.py
│   │   ├── middleware.py        # Request/response middleware
│   │   ├── requests.py          # Request utilities
│   │   ├── responses.py         # Response utilities
│   │   ├── routes.py            # Route registration
│   │   └── swagger.py           # API documentation
│   │
│   ├── domain/                  # Domain Layer (Business Logic)
│   │   ├── models/              # Business entities
│   │   │   ├── assessment_receipt.py
│   │   │   ├── assessment_request.py
│   │   │   ├── assessment_result.py
│   │   │   ├── certificate.py
│   │   │   ├── manager_approval.py
│   │   │   ├── service.py
│   │   │   └── user.py
│   │   ├── constants.py         # Business constants
│   │   └── exceptions.py        # Custom exceptions
│   │
│   ├── infrastructure/          # Infrastructure Layer (Data Access)
│   │   ├── databases/           # Database connections
│   │   │   ├── __init__.py
│   │   │   ├── base.py          # Base database config
│   │   │   ├── database.py      # Database factory
│   │   │   ├── mssql.py         # code de chay trong sql sever
│   │   │   └── sql_server.py    # neu dung mssql thì hay chinh sua code nay
│   │   ├── models/              # ORM models (SQLAlchemy)
│   │   │   ├── __init__.py
│   │   │   ├── assessment_receipt.py
│   │   │   ├── assessment_request.py
│   │   │   ├── assessment_result.py
│   │   │   ├── certificate.py
│   │   │   ├── manager_approval.py
│   │   │   ├── service.py
│   │   │   └── user.py
│   │   ├── repositories/        # Data access layer
│   │   │   ├── assessment_receipt_repository.py
│   │   │   ├── assessment_request_repository.py
│   │   │   ├── assessment_result_repository.py
│   │   │   ├── certificate_repository.py
│   │   │   ├── manager_approval_repository.py
│   │   │   ├── service_repository.py
│   │   │   └── user_repository.py
│   │   └── services/            # (Empty - services moved to root)
│   │
│   ├── services/                # Application Services Layer
│   │   ├── assessment_receipt_service.py
│   │   ├── assessment_request_service.py
│   │   ├── assessment_result_service.py
│   │   ├── certificate_service.py
│   │   ├── manager_approval_service.py
│   │   ├── service_service.py
│   │   └── user_service.py
│   │
│   ├── migrations/              # Database migrations
│   ├── instance/                # Instance-specific files
│   │
│   ├── app.py                   # Application entry point
│   ├── create_app.py            # Application factory
│   ├── config.py                # Configuration management
│   ├── dependency_container.py  # Dependency injection
│   ├── cors.py                  # CORS configuration
│   ├── app_logging.py           # Logging setup
│   ├── error_handler.py         # Global error handling
│   ├── default.db               # SQLite database
│   ├── requirements.txt         # Python dependencies
│   ├── swagger_config.json      # Swagger configuration
│   └── README.md                # Source documentation
│
├── venv/                        # Virtual environment
├── default.db                   # Database file
└── README.md                    # Project documentation
```




