# Handles summary calculations

from storage import load_expenses

# Total Summary
def total_summary():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found!")
        return

    total = sum(e['amount'] for e in expenses)
    print(f"Total Expenses: ${total}")