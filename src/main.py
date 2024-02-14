from fastapi import FastAPI
from src.routes import user, company

app = FastAPI()

app.include_router(user.route)
app.include_router(company.route)
@app.get("/")
async def root():
    return {"message": "Hello World2"}