from pydantic import BaseModel


class PurchaseBase(BaseModel):
    code: int
    announcement_id: int
    buyer_id: int
    seller_id: int
    price: float
    status: int




class PurchaseCreate(PurchaseBase):
    ...


class Purchase(PurchaseBase):
    id: int

    class Config:
        orm_mode = True