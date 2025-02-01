from sqlalchemy import Column, Integer, String,BigInteger
from database import Base


class User(Base):
    __tablename__ = 'Contact'

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, index=True)
    contact = Column(BigInteger,index=True)
    Email = Column(String, unique=True, index=True)
    Address = Column(String,index=True)








