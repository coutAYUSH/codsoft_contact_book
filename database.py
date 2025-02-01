from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

# Database URL (adjust as needed)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres.fastapi@localhost:5432/Event"

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for the models
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()  # Open a session
    try:
        yield db  # Yield the session to be used in the route
    finally:
        db.close()  # Close the session after the request is done
