# Core logic

import json
from datetime import datetime
from storage import load_expenses, save_expenses

# Add Expense
def add_expense(description, amount):
    expenses = load_expenses()

    new_id = max((e['id'] for e in expenses), default=0) + 1

    new_expense = {
        "id": new_id,
        "description": description,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    expenses.append(new_expense)
    save_expenses(expenses)
    return new_expense


# List Expenses
def list_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found!")
        return
    
    print(f"{'ID':<5} {'Date':<12} {'Description':<20} {'Amount':<10}")
    print("-" * 60)
    for e in expenses:
        print(f"{e['id']:<5} {e['date']:<12} {e['description']:<20} ${e['amount']:<10}")


# Delete Expense
def delete_expense(id):
    expenses = load_expenses()

    new_expenses = [e for e in expenses if e['id'] != id]

    if len(new_expenses) == len(expenses):
        print ("Expense ID {id} not found!")
        return False

    save_expenses(expenses)
    return True