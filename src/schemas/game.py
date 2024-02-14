from pydantic import BaseModel


class GameBase(BaseModel):
    name: str
    company_id: int


class GameCreate(GameBase):
    ...


class Game(GameBase):
    id: int

    class Config:
        orm_mode = True