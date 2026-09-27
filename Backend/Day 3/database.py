# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Replace 'root' and 'your_password' with your local MySQL credentials
# Format: mysql+pymysql://username:password@host:port/database_name
DATABASE_URL = "mysql+pymysql://root:test123@localhost:3306/ml_backend_db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "SessionLocal" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our declarative models
class Base(DeclarativeBase):
    pass

# Dependency function to get a database session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()