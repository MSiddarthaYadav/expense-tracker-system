<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, Float
from database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    date = Column(String, nullable=False)
    note = Column(String, nullable=True)
=======
from sqlalchemy import Column, Integer, String, Float
from database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    date = Column(String, nullable=False)
    note = Column(String, nullable=True)
>>>>>>> f1a44a0aa673c6de0723c9422f15493972fead4e
