from sqlalchemy import Column, Integer, String
from app.database import Base
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index = True)
    phone = Column(String, index = True)

class Program(Base):
    __tablename__ = "program"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index = True)
    description = Column(String, index = True)
    period = Column(String, index = True)