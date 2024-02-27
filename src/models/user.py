from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text, DateTim
from sqlalchemy.sql import func

from src.models.base import Base

class User(Base):
    __tablename__= "user"
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

