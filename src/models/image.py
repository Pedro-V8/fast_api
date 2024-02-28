import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text, DateTime
from sqlalchemy.sql import func
from src.models.base import Base

from .announcement import Announcement

class Image(Base):
    __tablename__= "image"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    path = Column(String(100), nullable=False)
    announcement_id = Column(ForeignKey("announcement.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)