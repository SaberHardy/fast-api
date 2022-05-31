from sqlalchemy import create_engine  # where is our database and type db, filepath
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create database
engine = create_engine('sqlite:///todo.db')

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
