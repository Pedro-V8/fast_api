from fastapi import FastAPI
from src.routes import user, company, game, announcement, purchase, image

app = FastAPI()


app.include_router(user.route)
app.include_router(company.route)
app.include_router(game.route)
app.include_router(announcement.route)
app.include_router(purchase.route)
app.include_router(image.route)

@app.get("/")
async def root():
    return {"message": "Hello World"}