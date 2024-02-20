from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    age: int
    email: str
    password: str



class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int

    class Config:
        orm_mode = True