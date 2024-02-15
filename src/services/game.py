from fastapi import Depends
from src.repository.game import GameRepository

class GameService:
    def __init__(self , game_repository: GameRepository = Depends(GameRepository)):
        self.game_repository = game_repository

    def get_games(self):
        games = self.game_repository.get()
        return games

    def get_games_by_company(self, company_id: int):
        games = self.game_repository.get_by_company(company_id)
        return games
    
    def create_game(self, data):
        game = self.game_repository.create(data)
        
        return game
