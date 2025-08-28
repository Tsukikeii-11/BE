# Architecture

```bash
    ├── scripts
│   └── run_postgres.sh
├── src
│   ├── api
│   │   ├── controllers
│   │   │   ├── assessment_receipt_controller.py
│   │   │   ├── assessment_request_controller.py
│   │   │   ├── assessment_result_controller.py
│   │   │   ├── certificate_controller.py
│   │   │   ├── manager_approval_controller.py
│   │   │   ├── service_controller.py
│   │   │   └── user_controller.py
│   │   ├── schemas
│   │   │   ├── service_schema.py
│   │   │   └── user_schema.py
│   │   ├── middleware.py
│   │   ├── requests.py
│   │   ├── responses.py
│   │   ├── routes.py
│   │   └── swagger.py
│   ├── domain
│   │   ├── models
│   │   │   ├── assessment_receipt.py
│   │   │   ├── assessment_request.py
│   │   │   ├── assessment_result.py
│   │   │   ├── certificate.py
│   │   │   ├── manager_approval.py
│   │   │   ├── service.py
│   │   │   └── user.py
│   │   ├── constants.py
│   │   └── exceptions.py
│   ├── infrastructure
│   │   ├── databases
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── database.py
│   │   │   ├── mssql.py
│   │   │   └── sql_server.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── assessment_receipt.py
│   │   │   ├── assessment_request.py
│   │   │   ├── assessment_result.py
│   │   │   ├── certificate.py
│   │   │   ├── manager_approval.py
│   │   │   ├── service.py
│   │   │   └── user.py
│   │   ├── repositories
│   │   │   ├── assessment_receipt_repository.py
│   │   │   ├── assessment_request_repository.py
│   │   │   ├── assessment_result_repository.py
│   │   │   ├── certificate_repository.py
│   │   │   ├── manager_approval_repository.py
│   │   │   ├── service_repository.py
│   │   │   └── user_repository.py
│   │   └── services
│   │       ├── assessment_receipt_service.py
│   │       ├── assessment_request_service.py
│   │       ├── assessment_result_service.py
│   │       ├── certificate_service.py
│   │       ├── manager_approval_service.py
│   │       ├── service_service.py
│   │       └── user_service.py
│   ├── app_logging.py
│   ├── app.py
│   ├── config.py
│   ├── cors.py
│   ├── create_app.py
│   ├── default.db
│   ├── dependency_container.py
│   └── error_handler.py
├── migrations
├── README.md
├── requirements.txt
├── swagger_config.json
└── venv
    ├── Include
    ├── Lib
    ├── Scripts
    └── pyvenv.cfg


## Domain Layer

## Services Layer

## Infrastructure Layer

## Download source code (CMD)
    git clone https://github.com/ChienNguyensrdn/Flask-CleanArchitecture.git
## Kiểm tra đã cài python đã cài đặt trên máy chưa
    python --version
## Run app

 - Bước 1: Tạo môi trường ảo co Python (phiên bản 3.x)
     ## Windows:
     		py -m venv .venv
     ## Unix/MacOS:
     		python3 -m venv .venv
   - Bước 2: Kích hoạt môi trường:
     ## Windows:
     		.venv\Scripts\activate.ps1
     ### Nếu xảy ra lỗi active .venv trên winos run powshell -->Administrator
         Set-ExecutionPolicy RemoteSigned -Force
     ## Unix/MacOS:
     		source .venv/bin/activate
     
   - Bước 3: Cài đặt các thư viện cần thiết
     ## Install:
     		pip install -r requirements.txt
   - Bước 4: Chạy mã xử lý dữ liệu
     ## Run:
    		python app.py


     Truy câp http://localhost:6868/docs



## Create file .env in folder /src/.env
    
    # Flask settings
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
    
    # SQL Server settings
    DB_USER=sa
    DB_PASSWORD=Aa@123456
    DB_HOST=127.0.0.1
    DB_PORT=1433
    DB_NAME=FlaskApiDB
    
    
    DATABASE_URI = "mssql+pymssql://sa:Aa%40123456@127.0.0.1:1433/FlaskApiDB"

## pull image MS SQL server 
    
    ```bash
    docker pull mcr.microsoft.com/mssql/server:2025-latest
    ```
## Install MS SQL server in docker 
    ```bash
    docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=Aa123456" -p 1433:1433 --name sql1 --hostname sql1 -d  mcr.microsoft.com/mssql/server:2025-latest
    ```
## Test connect SQL server 

## ORM Flask (from sqlalchemy.orm )
Object Relational Mapping

Ánh xạ 1 class (OOP)  model src/infrastructure/models --> Table in database 
Ánh xạ các mối quan hệ (Relational) -- Khoá ngoại CSDL 
(n-n): many to many 
# BE
BE dự án CNPM (flask api python)

