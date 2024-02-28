from fastapi import APIRouter, Depends , File, UploadFile
from src.services.image import ImageService

import uuid

route = APIRouter()

@route.post("/upload_image")
async def upload_image(
    image_service: ImageService = Depends(ImageService),
    file: UploadFile = File(...)
):
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()

    response = image_service.save_image(contents , file)

    return response

