from email.mime import base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()


class Booking(Base):

    __tablename__= "Booking"
    id= Column(Integer,primary_key = True, index = True)
    customer_name= Column(String,)
    phone= Column(String)
    event_type= Column(String)
    booking_date= Column(String)
    mehendi_type= Column(String)
    price= Column(String)
    status= Column(String)

class Review(Base):
class User(Base):
