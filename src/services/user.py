from fastapi import Depends
from src.repository.user import UserRepository

class UserService:
    def __init__(self , user_repository: UserRepository = Depends(UserRepository)):
        self.user_repository = user_repository

    def get_users(self):
        users = self.user_repository.get()
        return users
    
    def get_user_by_username(self, username: str):
        user = self.user_repository.get_one(username)
        return user
    
    def create_user(self, data):
        user = self.user_repository.create(data)
        
        return user
