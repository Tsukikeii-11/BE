# Architecture

```bash
# === Scripts ===
├── scripts                     # Chứa các script tiện ích, ví dụ chạy DB
│   └── run_postgres.sh

# === Source Code ===
├── src
│   ├── api                      # Layer API: controllers + schemas + middleware + routes
│   │   ├── controllers          # Controllers: xử lý request/response
│   │   │   ├── assessment_receipt_controller.py
│   │   │   ├── assessment_request_controller.py
│   │   │   ├── assessment_result_controller.py
│   │   │   ├── certificate_controller.py
│   │   │   ├── manager_approval_controller.py
│   │   │   ├── service_controller.py
│   │   │   └── user_controller.py
│   │   ├── schemas              # Marshmallow schemas: validate + serialize/deserialize
│   │   │   ├── service_schema.py
│   │   │   └── user_schema.py
│   │   ├── middleware.py        # Middleware chung
│   │   ├── requests.py          # Request helper
│   │   ├── responses.py         # Response helper
│   │   ├── routes.py            # Đăng ký route cho app
│   │   └── swagger.py           # Cấu hình Swagger/OpenAPI

# === Domain Layer ===
│   ├── domain
│   │   ├── models               # Business logic models
│   │   │   ├── assessment_receipt.py
│   │   │   ├── assessment_request.py
│   │   │   ├── assessment_result.py
│   │   │   ├── certificate.py
│   │   │   ├── manager_approval.py
│   │   │   ├── service.py
│   │   │   └── user.py
│   │   ├── constants.py         # Hằng số của dự án
│   │   └── exceptions.py        # Exception custom

# === Infrastructure Layer ===
│   ├── infrastructure
│   │   ├── databases            # ORM, DB connection, adapter
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── database.py
│   │   │   ├── mssql.py
│   │   │   └── sql_server.py
│   │   ├── models                # Database models
│   │   │   ├── __init__.py
│   │   │   ├── assessment_receipt.py
│   │   │   ├── assessment_request.py
│   │   │   ├── assessment_result.py
│   │   │   ├── certificate.py
│   │   │   ├── manager_approval.py
│   │   │   ├── service.py
│   │   │   └── user.py
│   │   ├── repositories          # CRUD DB, tương tác trực tiếp với DB
│   │   │   ├── assessment_receipt_repository.py
│   │   │   ├── assessment_request_repository.py
│   │   │   ├── assessment_result_repository.py
│   │   │   ├── certificate_repository.py
│   │   │   ├── manager_approval_repository.py
│   │   │   ├── service_repository.py
│   │   │   └── user_repository.py
│   │   └── services              # Service liên kết domain với repository
│   │       ├── assessment_receipt_service.py
│   │       ├── assessment_request_service.py
│   │       ├── assessment_result_service.py
│   │       ├── certificate_service.py
│   │       ├── manager_approval_service.py
│   │       ├── service_service.py
│   │       └── user_service.py

# === App setup & configs ===
│   ├── app_logging.py
│   ├── app.py
│   ├── config.py
│   ├── cors.py
│   ├── create_app.py
│   ├── default.db
│   ├── dependency_container.py
│   └── error_handler.py

# === Other ===
├── migrations                   # Alembic hoặc Flask-Migrate
├── README.md
├── requirements.txt
├── swagger_config.json
└── venv                          # Virtual environment
    ├── Include
    ├── Lib
    ├── Scripts
    └── pyvenv.cfg
