from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text, DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import FLOAT
from src.models.base import Base

from .game import Game
from .user import User


class Announcement(Base):
    __tablename__= "announcement"
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(String(500), nullable=False)
    price = Column(FLOAT(precision=2))
    user_id = Column(ForeignKey("user.id"))
    game_id = Column(ForeignKey("game.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

