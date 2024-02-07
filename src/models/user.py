from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from src.models.base import Base

class User(Base):
    __tablename__= "user"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)

