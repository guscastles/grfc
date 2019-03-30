# coding: utf-8
"""
Database creation
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class Players(Base):
    """Players' details table"""

    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
 

if __name__ == '__main__':
    engine = create_engine("sqlite:///grfc.db")
    Base.metadata.create_all(engine)
