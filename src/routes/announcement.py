from fastapi import APIRouter, Depends

from src.services.announcement import AnnouncementService
from src.schemas.announcement import AnnouncementBase, AnnouncementCreate         

route = APIRouter()

@route.get("/announcements")
def return_all_announcements(
    announcement_service: AnnouncementService = Depends(AnnouncementService)
):
    response = announcement_service.get_Announcements()

    return response


@route.post("/create_announcement", status_code=201)
def create_Announcement(
    request_data: AnnouncementCreate,
    announcement_service: AnnouncementService = Depends(AnnouncementService)
):
    response = announcement_service.create_game(request_data)

    return response
