from fastapi import APIRouter, Depends

from src.services.user import UserService
from src.schemas.user import UserBase, UserCreate


route = APIRouter()

@route.get("/users")
def return_all_users(
    user_service: UserService = Depends(UserService)
):
    response = user_service.get_users()

    return response

@route.post("/create_user", status_code=201)
def create_user(
    request_data: UserCreate,
    user_service: UserService = Depends(UserService)
):
    response = user_service.create_user(request_data)

    return response
