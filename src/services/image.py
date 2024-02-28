from fastapi import Depends
from src.repository.image import ImageRepository

class ImageService:
    def __init__(self , image_repository: ImageRepository = Depends(ImageRepository)):
        self.image_repository = image_repository

    def save_image(self, data, file):
        with open(f"images/{file.filename}", "wb") as f:
            f.write(data)

        
        #image = self.image_repository.save(data)
        return True