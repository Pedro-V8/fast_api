import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text, DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import FLOAT
from src.models.base import Base

from .announcement import Announcement
from .user import User

class StatusType(enum.Enum):
    active = 0
    paused = 1
    finished = 2
class Purchase(Base):
    __tablename__= "purchase"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer, nullable=False)
    announcement_id = Column(ForeignKey("announcement.id"))
    buyer_id = Column(ForeignKey("user.id"))
    seller_id = Column(ForeignKey("user.id"))
    price = Column(FLOAT(precision=2))
    status = Column(Enum(StatusType))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

