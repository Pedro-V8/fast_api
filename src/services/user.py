import os

from datetime import datetime , timedelta
from fastapi import Depends
from dotenv import load_dotenv
from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import Union, Any

from src.repository.user import UserRepository


load_dotenv()

class UserService:
    def __init__(self , user_repository: UserRepository = Depends(UserRepository)):
        self.user_repository = user_repository
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_users(self):
        users = self.user_repository.get()
        return users
    
    def get_user_by_username(self, username: str):
        user = self.user_repository.get_one(username)
        return user
    
    def create_user(self, data):
        data.password = self.get_hashed_password(data.password)
    
        user = self.user_repository.create(data)
        
        return user
    
    def get_hashed_password(self, password: str) -> str:
        return self.pwd_context.hash(password)
    
    def verify_password(self, password:str, hash_password: str) -> bool:
        return self.pwd_context.verify(password, hash_password)
    
    def create_access_token(self, subject: Union[str, Any], expires_delta: int = None) -> str:
        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow() + timedelta(minutes=30)
        
        
            
        to_encode = {"exp": expires_delta, "sub": str(subject)}

        encoded_jwt = jwt.encode(to_encode, "narscbjim@$@&^@&%^&RFghgjvbdsha", "HS256")
        
        return encoded_jwt

    def create_refresh_token(self, subject: Union[str, Any], expires_delta: int = None) -> str:
        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow() + timedelta(minutes=30)
        
        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, "13ugfdfgh@#$%^@&jkl45678902", "HS256")
        return encoded_jwt

    def login(self, data):

        user = self.user_repository.get_one(data.email)

        if not user:
            return False

        hashed_pass = user.password

        if not self.verify_password(data.password , hashed_pass):
            return False
        
        access = self.create_access_token(user.id)
        refresh = self.create_refresh_token(user.id)

        self.user_repository.create_token(user.id, access, refresh)
        
        return {
            "access_token": access,
            "refresh_token": refresh,
        }
