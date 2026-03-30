# 💰 Expense Tracker CLI

A simple command-line interface (CLI) application to track and manage your daily expenses. Built with Python — no external libraries required.

---

## 📋 Features

- ✅ Add new expenses with description and amount
- ✏️ Update existing expenses
- 🗑️ Delete expenses by ID
- 📄 View all expenses in a formatted table
- 📊 View total expense summary
- 📅 View monthly expense summary
- 🏷️ Categorize expenses

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your machine
- No external libraries needed

### Installation

1. Clone the repository:

```bash
   git clone https://github.com/Dhanuka-Wimalarathna/Python-Mini-Projects.git
```

2. Navigate to the project folder:

```bash
   cd Python-Mini-Projects/Expense_Tracker
```

3. Run the application:

```bash
   python expense_tracker.py
```

---

## 💻 Usage

### Add an Expense

```bash
python expense_tracker.py add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)
```

### Add an Expense with Category

```bash
python expense_tracker.py add --description "Lunch" --amount 20 --category "Food"
# Expense added successfully (ID: 1)
```

### List All Expenses

```bash
python expense_tracker.py list
# ID    Date         Description          Amount
# ----------------------------------------------------
# 1     2026-03-30   Lunch                $20.0
# 2     2026-03-30   Dinner               $10.0
```

### Update an Expense

```bash
python expense_tracker.py update --id 1 --description "Breakfast" --amount 15
# Expense updated successfully (ID: 1)
```

### Delete an Expense

```bash
python expense_tracker.py delete --id 1
# Expense deleted successfully
```

### View Total Summary

```bash
python expense_tracker.py summary
# Total expenses: $30.0
```

### View Monthly Summary

```bash
python expense_tracker.py summary --month 3
# Total expenses for March: $30.0
```

---

## 🗂️ Expense Properties

Each expense stored in `expenses.json` has the following properties:

| Property      | Description                       |
| ------------- | --------------------------------- |
| `id`          | Unique identifier for the expense |
| `description` | Short description of the expense  |
| `amount`      | Cost of the expense               |
| `date`        | Date the expense was added        |
| `category`    | Category of the expense           |

### Example `expenses.json`

```json
[
  {
    "id": 1,
    "description": "Lunch",
    "amount": 20.0,
    "date": "2026-03-30",
    "category": "Food"
  },
  {
    "id": 2,
    "description": "Dinner",
    "amount": 10.0,
    "date": "2026-03-30",
    "category": "Food"
  }
]
```

---

## 📁 Project Structure

```
Expense_Tracker/
│
├── expense_tracker.py   # Main entry point - handles CLI commands
├── expenses.py          # Core logic - add, delete, update, view
├── storage.py           # Handles reading/writing JSON file
├── summary.py           # Handles summary calculations
├── expenses.json        # Auto-generated data storage file
└── README.md            # Project documentation
```

---

## ⚙️ How It Works

- Expenses are stored locally in an `expenses.json` file
- The file is **automatically created** if it does not exist
- No database or internet connection is required
- Uses only Python's built-in `json`, `os`, and `datetime` modules

---

## 🛠️ Built With

- **Python 3** — Programming language
- **argparse** — Built-in module for parsing CLI arguments
- **json** — Built-in module for reading/writing JSON
- **datetime** — Built-in module for timestamps

---

## 📌 Project Inspiration

This project is inspired by the [Expense Tracker](https://roadmap.sh/projects/expense-tracker) project on roadmap.sh.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
