#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: shaunahan
"""

#use engines and sessions to connect and edit a database. 

# Import the function needed
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Create the engine
engine = create_engine("postgresql+psycopg2://dcstudent:S3cretPassw0rd@localhost:5432/campdata-prod")

# Create the session
session = Session(engine)

# define a python class to create a SQL table.

# Import the objects needed
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer

# Initialize the base and set inheritance
# base object has metadata about the schema and tables

Base = declarative_base()

#map a class to a PostgreSQL table, declaring a table name and a primary key.

class PprRawAll(Base):
    #set the table name
    __tablename__ = "ppr_raw_all"
    
    #string columns can hold up to 55 characters, except for the address that should be able  to hold up to 255 characters.
    id = Column(Integer, primary_key=True)
    date_of_sale = Column(String(55))
    address = Column(String(255))
    postal_code = Column(String(55))
    county = Column(String(55))
    price = Column(String(55))
    description = Column(String(55))
    
