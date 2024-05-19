from sqlalchemy import create_engine, Column, String, Date, Float, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from schemas.currency import Base

engine = create_engine('sqlite:///exchanges.sqlite:', echo=True)

Base.metadata.create_all(engine)
