# Handles summary calculations

from storage import load_expenses

# Total Summary
def total_summary():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found!")
        return

    total = sum(e['amount'] for e in expenses)
    print(f"Total Expenses: Rs.{total}")


# Monthly Summary
def monthly_summary():
    expenses = load_expenses()

    monthly_expenses = [
        e for e in expenses if int(e['date'].split('-')[1]) == month
    ]

    if not monthly_expenses:
        print("No expenses found for this {month}!")
        return

    total = sum(e['amount'] for e in monthly_expenses)

    month_names = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    print(f"Monthly Expenses (Month {month}): Rs.{total}")