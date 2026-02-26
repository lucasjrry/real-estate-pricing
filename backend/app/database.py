from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# This will create a local SQLite file named real_estate.db in your backend folder
SQLALCHEMY_DATABASE_URL = "sqlite:///./real_estate.db"

# connect_args={"check_same_thread": False} is required for SQLite in FastAPI
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get a database session for our API routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()