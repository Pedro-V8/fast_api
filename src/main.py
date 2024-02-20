from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.routes import user

from jose import JWTError, jwt


app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], depreacted="auto")

app.include_router(user.route)
@app.get("/")
async def root():
    return {"message": "Hello World2"}