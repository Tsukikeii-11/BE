from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config import Config
from src.infrastructure.databases.base import Base

# Database configuration
DATABASE_URL = Config.DATABASE_URI
print(DATABASE_URL)
# Create a new SQLAlchemy engine instance
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_mssql(app):
    # Import all modules here that might define models so that
    # they will be registered properly on the metadata.
    # This is necessary to avoid circular imports.
    

    # Create the database tables
    Base.metadata.create_all(bind=engine)