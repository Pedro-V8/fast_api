from fastapi import Depends

from src.db.session import SessionLocal , get_db
from src.models.announcement import Announcement

class AnnouncementRepository:
    def __init__(self, db: SessionLocal = Depends(get_db)) -> None:
        self.db = db

    def get(self) -> Announcement:
        return self.db.query(Announcement).all()


    def create(self, data):
        announcement_model = Announcement(
            title=data.title, 
            description=data.description, 
            price=data.price, 
            user_id=data.user_id, 
            game_id=data.game_id
        )
        self.db.add(announcement_model)
        self.db.commit()
        self.db.refresh(announcement_model)

        return announcement_model

