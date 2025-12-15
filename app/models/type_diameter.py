from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): 
    pass

class TypeDiameter(Base):
    __tablename__ = 'type_diameter'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=True)