from fastapi import Depends

from src.db.session import SessionLocal , get_db
from src.models.user import User

class UserRepository:
    def __init__(self, db: SessionLocal = Depends(get_db)) -> None:
        self.db = db

    def get(self) -> User:
        return self.db.query(User).all()
    
    def get_one(self, username: str) -> User:
        return self.db.query(User).filter_by(username)

    def create(self, data):
        user_model = User(name=data.name , age=data.age, email=data.email, password=data.password)
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)

        return user_model

