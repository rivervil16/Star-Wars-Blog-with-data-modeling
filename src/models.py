import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    userId = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)


class FavoritePlanet(Base):
    __tablename__ = 'favoriteplanet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('Planet.id'))



class FavoriteCharacter(Base):
    __tablename__ = 'favoritecharacter'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('Character.id'))

class Planet(Base):
    __tablename__ = 'Planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    weather = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    #diameter = Column(Integer, ForeignKey('user.id'))
    #weather = Column(Integer, ForeignKey('user.id'))
    #population = Column(Integer, ForeignKey('user.id'))

class Character(Base):
    __tablename__ = 'Character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    skincolor = Column(String(250), nullable=False)
    eyecolor = Column(String(250), nullable=False)


    def to_dict(self):
        return {}
        
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')