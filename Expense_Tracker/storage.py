# Handles reading/writing JSON file

import os
import json

DATA_FILE = 'expenses.json'

# Loading Expenses
def load_expenses():
    try:
        with open (DATA_FILE, 'r') as file:
            content = file.read().strip()
            if not content:
                return[]
            return json.loads(content)
    except FileNotFoundError:
        return[]


# Saving Expenses
def save_expenses(expenses):
    with open (DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)
        
