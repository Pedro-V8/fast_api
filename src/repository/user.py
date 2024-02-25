from fastapi import Depends

from src.db.session import SessionLocal , get_db
from src.models.user import User
from src.models.token import Token

class UserRepository:
    def __init__(self, db: SessionLocal = Depends(get_db)) -> None:
        self.db = db

    def get(self) -> User:
        return self.db.query(User).all()
    
    def get_one(self, username: str) -> User:
        return self.db.query(User).filter(User.email == username).first()

    def create(self, data):
        user_model = User(name=data.name , age=data.age, email=data.email, password=data.password)
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)

        return user_model

    def create_token(self, userid, accesstoken, refreshtoken):
        token_model = Token(user_id=userid , access_token=accesstoken, refresh_token=refreshtoken, status=True)
        self.db.add(token_model)
        self.db.commit()
        self.db.refresh(token_model)

        return token_model

