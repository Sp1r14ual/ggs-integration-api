from sqlalchemy import Column, Integer, BigInteger, Numeric, String, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): 
    pass

class Equip(Base):
    __tablename__ = 'equip'

    id = Column(Integer, primary_key=True, nullable=False)
    id_type_packing = Column(Integer, ForeignKey('type_packing.id'))
    length = Column(Numeric(precision=8, scale=2), nullable=True)
    id_type_diameter = Column(Integer, ForeignKey('type_diameter.id'))
    amount = Column(Integer, nullable=True)
    id_type_pipe_material = Column(Integer, ForeignKey('type_pipe_material.id'))
    diameter = Column(Numeric(precision=8, scale=2), nullable=True)
    num = Column(Integer, nullable=True)
    equip_crm_id = Column(Integer, nullable=True)


