from pydantic import BaseModel


class ExpenseCreate(BaseModel):
    amount: float
    category: str
    date: str
    note: str = ""


class ExpenseOut(BaseModel):
    id: int
    amount: float
    category: str
    date: str
    note: str = ""

    class Config:
        from_attributes = True
