from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time 
from .config import settings

"""
format: 
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost/db_name"

"""

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#request database session dependency , when it done it will close the session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
# max_retries = 5
# retry_count = 0

# while retry_count < max_retries:
#     try: 
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='admin098', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as error:
#         retry_count += 1
#         print(f"Connecting to database failed! (Attempt {retry_count}/{max_retries})")
#         print("Error: ", error)
#         if retry_count < max_retries:
#             time.sleep(2)
#         else:
#             raise Exception("Failed to connect to database after maximum retries")