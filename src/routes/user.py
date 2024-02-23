from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
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


@route.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), user_service: UserService = Depends(UserService)):
    user = user_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        return {"error": True}
    access_token_expires = timedelta(minutes=15)
    access_token = user_service.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}