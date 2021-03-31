import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password =  Column(String(250), nullable=False)
    created = Column(DateTime, nullable=False)
    edited = Column(DateTime, nullable=False)
    createdBy = Column(String(250), nullable=False)
    editedBy = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(Boolean, nullable=False)
    population = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False)
    edited = Column(DateTime, nullable=False)
    createdBy = Column(String(250), nullable=False)
    editedBy = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(Date, nullable=False)
    gender = Column(String(250), nullable=False)
    created = Column(DateTime, nullable=False)
    edited = Column(DateTime, nullable=False)
    createdBy = Column(String(250), nullable=False)
    editedBy = Column(String(250), nullable=False)



class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    
    User = Column(Integer, ForeignKey('user.id'))
    user_id = Column(Integer, ForeignKey('person.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    created = Column(DateTime, nullable=False)
    edited = Column(DateTime, nullable=False)
    createdBy = Column(String(250), nullable=False)
    editedBy = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')