from fastapi import APIRouter, Depends

from src.services.purchase import PurchaseService
from src.schemas.purchase import PurchaseBase, PurchaseCreate         

route = APIRouter()

@route.get("/purchases")
def return_all_Purchases(
    purchase_service: PurchaseService = Depends(PurchaseService)
):
    response = purchase_service.get_purchases()

    return response


@route.post("/create_purchase", status_code=201)
def create_Purchase(
    request_data: PurchaseCreate,
    purchase_service: PurchaseService = Depends(PurchaseService)
):
    response = purchase_service.create_purchase(request_data)

    return response
