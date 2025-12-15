from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): 
    pass

class TypeBoilSetup(Base):
    __tablename__ = 'type_boil_setup'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=True)