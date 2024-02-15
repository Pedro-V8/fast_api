from fastapi import APIRouter, Depends

from src.services.game import GameService
from src.schemas.game import GameBase, GameCreate


route = APIRouter()

@route.get("/games")
def return_all_games(
    game_service: GameService = Depends(GameService)
):
    response = game_service.get_games()

    return response

@route.get("/games_by_company/{company_id}")
def return_all_games_by_company(
    company_id: int,
    game_service: GameService = Depends(GameService)
):
    response = game_service.get_games_by_company(company_id)

    return response

@route.post("/create_game", status_code=201)
def create_game(
    request_data: GameCreate,
    game_service: GameService = Depends(GameService)
):
    response = game_service.create_game(request_data)

    return response
