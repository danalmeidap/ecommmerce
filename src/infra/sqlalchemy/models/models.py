from src.infra.sqlalchemy.config.database import Base
from sqlalchemy import Integer, Column, String, Float, DateTime
from datetime import datetime


class Product(Base):

    __tablename__= "product"

    id= Column(Integer, primary_key=True, index=True)
    name= Column(String)
    price= Column(Float)
    score= Column(Integer)
    created= Column(DateTime, default=datetime.now)
