from pydantic import BaseModel


class AnnouncementBase(BaseModel):
    title: str
    description: str
    price: float
    user_id: int
    game_id: int



class AnnouncementCreate(AnnouncementBase):
    ...


class Announcement(AnnouncementBase):
    id: int

    class Config:
        orm_mode = True