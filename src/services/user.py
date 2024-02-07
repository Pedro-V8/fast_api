from fastapi import Depends
from src.repository.user import UserRepository

class UserService:
    def __init__(self , user_repository: UserRepository = Depends(UserRepository)):
        self.user_repository = user_repository

    def get_users(self):
        users = self.user_repository.get()
        return users
    
    def create_user(self, data):
        user = self.user_repository.create(data)
        
        return user
