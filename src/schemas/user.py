from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    age: int


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int

    class Config:
        orm_mode = True