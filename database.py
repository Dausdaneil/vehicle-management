from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:yourpassword@localhost/vehicle_db"

# Create engine
engine = create_engine(DATABASE_URL)

# SessionLocal class to use in my app
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


# Test DB connection
def test_db_connection():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("✅ Connected to DB")
    except Exception as e:
        print("❌ Failed to connect to DB")
        print("Error:", e)


# Run test
test_db_connection()
