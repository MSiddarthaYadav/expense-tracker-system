<<<<<<< HEAD
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
=======
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
>>>>>>> f1a44a0aa673c6de0723c9422f15493972fead4e
