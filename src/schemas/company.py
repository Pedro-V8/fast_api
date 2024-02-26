from pydantic import BaseModel


class CompanyBase(BaseModel):
    name: str


class CompanyCreate(CompanyBase):
    ...


class Company(CompanyBase):
    id: int

    class Config:
        orm_mode = True