from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text, DateTime
from sqlalchemy.sql import func
from src.models.base import Base
from src.models.user import User

class Token(Base):
    __tablename__= "token"
    
    user_id = Column(Integer, ForeignKey("user.id"))
    access_token = Column(String(450), primary_key=True)
    refresh_token = Column(String(450),nullable=False)
    status = Column(Boolean)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

