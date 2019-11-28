from config import SQLALCHEMY_DATABASE_URI

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

Base = declarative_base()

DB_session = sessionmaker(bind=engine)

session = DB_session()
