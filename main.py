<<<<<<< HEAD
from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException


from database import SessionLocal, engine
from models import Expense
from schemas import ExpenseCreate, ExpenseOut
from database import Base

app = FastAPI(title="Expense Tracker")

# Create tables
Base.metadata.create_all(bind=engine)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/expenses", response_model=ExpenseOut)
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = Expense(
        amount=expense.amount,
        category=expense.category,
        date=expense.date,
        note=expense.note
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


@app.get("/expenses", response_model=list[ExpenseOut])
def get_expenses(db: Session = Depends(get_db)):
    expenses = db.query(Expense).order_by(Expense.id.desc()).all()
    return expenses


@app.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    total = db.query(func.sum(Expense.amount)).scalar() or 0
    return {"total_spent": float(total)}

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(expense)
    db.commit()
    return {"message": "Expense deleted successfully"}

=======
from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException


from database import SessionLocal, engine
from models import Expense
from schemas import ExpenseCreate, ExpenseOut
from database import Base

app = FastAPI(title="Expense Tracker")

# Create tables
Base.metadata.create_all(bind=engine)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/expenses", response_model=ExpenseOut)
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = Expense(
        amount=expense.amount,
        category=expense.category,
        date=expense.date,
        note=expense.note
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


@app.get("/expenses", response_model=list[ExpenseOut])
def get_expenses(db: Session = Depends(get_db)):
    expenses = db.query(Expense).order_by(Expense.id.desc()).all()
    return expenses


@app.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    total = db.query(func.sum(Expense.amount)).scalar() or 0
    return {"total_spent": float(total)}

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(expense)
    db.commit()
    return {"message": "Expense deleted successfully"}

>>>>>>> f1a44a0aa673c6de0723c9422f15493972fead4e
