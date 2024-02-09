from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from src.models.base import Base

class Game(Base):
    __tablename__= "game"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    company = Column(String(50), nullable=False)

