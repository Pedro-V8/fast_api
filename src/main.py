from fastapi import FastAPI
from src.routes import user

app = FastAPI()


app.include_router(user.route)
@app.get("/")
async def root():
    return {"message": "Hello World2"}