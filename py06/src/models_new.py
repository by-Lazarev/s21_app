# models.py

from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Spaceship(Base):
    __tablename__ = 'spaceships'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    alignment = Column(String, nullable=False)
    ship_class = Column(String, nullable=False)
    length = Column(Float, nullable=False)
    crew_size = Column(Integer, nullable=False)
    armed = Column(Boolean, nullable=False)
    
    officers = relationship("Officer", back_populates="spaceship", cascade="all, delete-orphan")
    
    UniqueConstraint('name', 'alignment', name='uq_spaceship_name_alignment')

class Officer(Base):
    __tablename__ = 'officers'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    rank = Column(String, nullable=False)
    spaceship_id = Column(Integer, ForeignKey('spaceships.id'), nullable=False)
    
    spaceship = relationship("Spaceship", back_populates="officers")
    
    UniqueConstraint('first_name', 'last_name', 'rank', 'spaceship_id', name='uq_officer_identity')

