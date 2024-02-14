from fastapi import Depends

from src.db.session import SessionLocal , get_db
from src.models.company import Company

class CompanyRepository:
    def __init__(self, db: SessionLocal = Depends(get_db)) -> None:
        self.db = db

    def get(self) -> Company:
        return self.db.query(Company).all()

    def create(self, data):
        company_model = Company(name=data.name)
        self.db.add(company_model)
        self.db.commit()
        self.db.refresh(company_model)

        return company_model

