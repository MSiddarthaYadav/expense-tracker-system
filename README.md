💰 Expense Tracker - FastAPI

A simple and efficient Expense Tracker Web Application built using FastAPI and SQLAlchemy.
This project helps users add, view, delete expenses, and track their total spending summary.

🚀 Features

✅ Add new expenses (amount, category, date, note)

📋 View all expenses (latest first)

🗑️ Delete an expense by ID

📊 Get total spending summary

🌐 Simple frontend using HTML

📌 FastAPI interactive API docs available

🛠 Tech Stack

Backend: FastAPI (Python)

Database: SQLAlchemy + SQLite

Validation: Pydantic Schemas

Frontend: HTML, CSS

Server: Uvicorn

📂 Project Structure
expense-tracker-fastapi/
│── main.py
│── database.py
│── models.py
│── schemas.py
│── templates/
│    └── index.html
│── static/
│    └── (css/js/images)
│── requirements.txt

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2️⃣ Create Virtual Environment (Recommended)
python -m venv myenv
myenv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt


If you don’t have requirements.txt, install manually:

pip install fastapi uvicorn sqlalchemy

▶️ Run the Project

Start the server:

uvicorn main:app --reload


If uvicorn command doesn’t work, run:

python -m uvicorn main:app --reload


Server will run at:

http://127.0.0.1:8000

🌐 API Endpoints
Method	Endpoint	Description
GET	/	Loads the frontend HTML page
POST	/expenses	Add a new expense
GET	/expenses	Get all expenses
GET	/summary	Get total spending summary
DELETE	/expenses/{expense_id}	Delete expense by ID
📌 API Documentation

FastAPI provides automatic documentation:

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc UI:
http://127.0.0.1:8000/redoc

🧪 Sample JSON for Adding Expense
{
  "amount": 250,
  "category": "Food",
  "date": "2026-01-22",
  "note": "Lunch"
}

📌 Future Improvements (Optional)

User login system (Authentication)

Monthly category-wise charts

Export expenses to Excel/PDF

Responsive UI improvements

👨‍💻 Author

Siddartha Yadav
📌 Expense Tracker - FastAPI Project
