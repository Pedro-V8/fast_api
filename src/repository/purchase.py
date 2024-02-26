from fastapi import Depends

from src.db.session import SessionLocal , get_db
from src.models.purchase import Purchase

class PurchaseRepository:
    def __init__(self, db: SessionLocal = Depends(get_db)) -> None:
        self.db = db

    def get(self) -> Purchase:
        return self.db.query(Purchase).all()


    def create(self, data):
        purchase_model = Purchase(
            code=data.code, 
            announcement_id=data.announcement_id, 
            buyer_id=data.buyer_id, 
            seller_id=data.seller_id, 
            price=data.price,
            status=data.status
        )
        self.db.add(purchase_model)
        self.db.commit()
        self.db.refresh(purchase_model)

        return purchase_model

