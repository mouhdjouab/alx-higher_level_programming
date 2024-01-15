#!/usr/bin/python3

# Python file  contains class definition of State

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column


Base = declarative_base()


class State(Base):
    """
    State class

    Attributes:
        id: Id state
        name: Name of state
    """
    __tablename__ = "states"
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable=False)
    name = Column(String(128), nullable=False)
