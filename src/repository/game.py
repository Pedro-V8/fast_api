from fastapi import Depends

from src.db.session import SessionLocal , get_db
from src.models.game import Game

class GameRepository:
    def __init__(self, db: SessionLocal = Depends(get_db)) -> None:
        self.db = db

    def get(self) -> Game:
        return self.db.query(Game).all()

    def get_by_company(self, company_id: int):
        games = self.db.query(Game).filter(Game.company_id==company_id).all()

        return games

    def create(self, data):
        game_model = Game(name=data.name, company_id=data.company_id)
        self.db.add(game_model)
        self.db.commit()
        self.db.refresh(game_model)

        return game_model

