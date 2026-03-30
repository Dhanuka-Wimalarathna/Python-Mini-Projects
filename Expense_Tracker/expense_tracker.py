# Main Entry Point

import argparse
from expenses import add_expense, list_expenses, delete_expense
from summary import total_summary, monthly_summary


def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add Expense Command
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True, help="Expense description")
    add_parser.add_argument("--amount", type=float, required=True, help="Expense amount")

    # List Expenses Command
    subparsers.add_parser("list", help="List all expenses")

    # Delete Expense Command
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", type=int, required=True, help="Expense ID")

    # Summary Command
    summary_parser = subparsers.add_parser("summary", help="Show expense summary")
    summary_parser.add_argument("--month", type=int, help="Month number (1-12)")

    # Parse Arguments
    args = parser.parse_args()

    # Execute Commands
    if args.command == "add":
        if args.amount <= 0:
            print("Error: Amount must be greater than 0!")
            return
        add_expense(args.description, args.amount)

    elif args.command == "list":
        list_expenses()

    elif args.command == "delete":
        delete_expense(args.id)

    elif args.command == "summary":
        if args.month:
            if args.month < 1 or args.month > 12:
                print("Error: Month must be between 1 and 12!")
                return
            monthly_summary(args.month)
        else:
            total_summary()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
