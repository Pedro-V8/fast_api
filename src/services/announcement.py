from fastapi import Depends
from src.repository.announcement import AnnouncementRepository

class AnnouncementService:
    def __init__(self , announcement_repository: AnnouncementRepository = Depends(AnnouncementRepository)):
        self.announcement_repository = announcement_repository

    def get_announcements(self):
        announcements = self.announcement_repository.get()
        return announcements

    
    def create_announcement(self, data):
        announcement = self.announcement_repository.create(data)
        
        return announcement
