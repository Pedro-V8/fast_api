from fastapi import Depends
from src.repository.purchase import PurchaseRepository

class PurchaseService:
    def __init__(self , purchase_repository: PurchaseRepository = Depends(PurchaseRepository)):
        self.purchase_repository = purchase_repository

    def get_games(self):
        purchases = self.purchase_repository.get()
        return purchases

    
    def create_game(self, data):
        purchase = self.purchase_repository.create(data)
        
        return purchase
