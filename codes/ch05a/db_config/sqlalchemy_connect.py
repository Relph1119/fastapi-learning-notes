from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "postgresql://postgres:root@localhost:5432/fcms"

engine = create_engine(DB_URL)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
