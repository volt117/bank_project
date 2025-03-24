# 🧮 Personal Finance Tracker (CLI)

A simple command-line application written in Python that allows users to track their personal finances: register, manage transactions, monitor budgets, and generate reports. It supports multiple currencies and provides clear data validation and logging.

---

## 🚀 Features

- ✅ User registration and authentication (with password hashing)
- ✅ Add/edit/delete transactions
- ✅ Budget tracking per category
- ✅ Monthly and filtered transaction reports
- ✅ Currency support and conversion
- ✅ Date-based calculations (days left in week/month)
- ✅ Full input validation with custom error handling
- ✅ Logging of transactions and errors

---

## 🧩 Project Structure

finance-tracker/
├── main.py                   # CLI interface
├── user_management.py        # User registration and authentication
├── finance.py                # Transaction management
├── budget.py                 # Budget setup and tracking
├── currency_management.py    # Currency conversion logic
├── datetime_management.py    # Date utilities
├── reporting.py              # Report generation
├── logging_management.py     # Logs and error tracking
├── input_validation.py       # Validates user input
└── README.md                 # Project description
---

## 🛠 Installation

1. Clone the repository
git clone https://github.com/your-username/finance-tracker.git
cd finance-tracker
2. Run the application
python main.py
No external dependencies required – only Python standard library.

---

## 📌 Usage

Commands available in CLI:
- register – Register new user
- add_transaction – Add a new transaction
- report – Generate monthly report
- exit – Exit the app

Example:
Enter command: register
Enter username: john
Enter password: ********
User john successfully registered.
---

## 📄 License
This project is open-source and free to use.

---

## 💡 Author
Developed with 💙 by Kyryll Surov :)) xoxo
