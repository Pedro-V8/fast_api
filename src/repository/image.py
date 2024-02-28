from fastapi import Depends

from src.db.session import SessionLocal , get_db
from src.models.image import Image

class ImageRepository:
    def __init__(self, db: SessionLocal = Depends(get_db)) -> None:
        self.db = db

    def get(self) -> Image:
        return self.db.query(Image).all()


