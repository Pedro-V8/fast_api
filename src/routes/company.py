from fastapi import APIRouter, Depends

from src.services.company import CompanyService
from src.schemas.company import CompanyBase, CompanyCreate


route = APIRouter()

@route.get("/companys")
def return_all_companys(
    company_service: CompanyService = Depends(CompanyService)
):
    response = company_service.get_companys()

    return response

@route.post("/create_company", status_code=201)
def create_company(
    request_data: CompanyCreate,
    company_service: CompanyService = Depends(CompanyService)
):
    response = company_service.create_company(request_data)

    return response
