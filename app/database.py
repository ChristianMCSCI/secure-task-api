from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

# SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"

#Create Engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}                                        
)

#Session local class
SessionLocal = sessionmaker(autocommit=False, autoflush=False)

#Base class for models
Base = declarative_base()

#Dependency for FASTAPI endpoints
def get_db():
    """
    Provide a database session for each request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()