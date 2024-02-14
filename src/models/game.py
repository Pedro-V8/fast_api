from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text, DateTime
from sqlalchemy.sql import func
from src.models.base import Base

from .company import Company

class Game(Base):
    __tablename__= "game"
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    company_id = Column(ForeignKey("company.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

