from fastapi import Depends
from src.repository.company import CompanyRepository

class CompanyService:
    def __init__(self , company_repository: CompanyRepository = Depends(CompanyRepository)):
        self.company_repository = company_repository

    def get_companys(self):
        comapnys = self.company_repository.get()
        return comapnys
    
    def create_company(self, data):
        company = self.company_repository.create(data)
        
        return company
