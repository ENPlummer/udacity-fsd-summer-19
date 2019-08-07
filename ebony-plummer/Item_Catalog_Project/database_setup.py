# Imports
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Catagory(Base):
    __tablename__ = 'catagory'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    @property
    def serialize(self):
        #Return object data in a easily serialized format.
        return {
        'name' : self.name,
        'id' : self.id,
        }


class StoreItem(Base):
    __tablename__ = "storeItem"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    genre = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    price = Column(String(10))
    catagory_id = Column(Integer, ForeignKey('catagory.id'))
    catagory = relationship(Catagory)


    @property
    def serialize(self):
        #Return object data in a easily serialized format.  
        return {
        'id' : self.id,
        'title' : self.title,
        'author' : self.author,
        'genre' : self.genre,
        'description' : self.description,   
        'price' : self.price,
        }    
"""
class MusicItem(Base):
    __tablename__ = "music_item"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    artist = Column(String(100), nullable=False)
    genre = Column(String(100), nullable=False)
    price = Column(String(10), nullable=False)
    store_catagory_id = Column(Integer, ForeignKey('catagory.id'))
    catagory = relationship(Catagory)


    @property
    def serialize(self):
        #Return object data in a easily serialized format. 
        return {
        'id' : self.id,
        'title' : self.title,
        'artist' : self.artist,
        'genre' : self.genre,
        'price' : self.price,
        }
    
class MovieItem(Base):
    __tablename__ = "movie_item"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    stars = Column(String(250), nullable=True)
    director = Column(String(100), nullable=False)
    genre = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    price = Column(String(10), nullable=False)
    store_catagory_id = Column(Integer, ForeignKey('catagory.id'))
    catagory = relationship(Catagory)

    @property
    def serialize(self):
    #Return object data in a easily serialized format.
        return {
        'id' : self.id,
        'title' : self.title,
        'genre' : self.genre,
        'description' : self.description,
        'price' : self.price
    }
    
"""
#Create Database

engine = create_engine('sqlite:///storeitems.db')

Base.metadata.create_all(engine)  
    