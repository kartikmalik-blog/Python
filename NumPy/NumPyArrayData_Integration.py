'''
Data Integration
Why: Load real-world data (e.g., expenses.json) into NumPy arrays for analysis (e.g., filter expenses, compute totals).

Key Concept:

Use json module to read JSON data, then convert to NumPy arrays with np.array.

'''

import numpy as np
import json

def load_expenses(json_file, condition=None, stat=None):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        amounts = [item['amount'] for item in data]
        arr = np.array(amounts, dtype=float)
        if condition is not None:
            arr = arr[arr > condition]
        if len(arr) == 0:
            return "Error: No elements after filtering"
        if stat == 'mean':
            return np.mean(arr)
        elif stat == 'median':
            return np.median(arr)
        elif stat == 'min':
            return np.min(arr)
        elif stat == 'max':
            return np.max(arr)
        return arr
    except (FileNotFoundError, KeyError, ValueError):
        return "Error: Invalid JSON file or data"

def create_sample_expenses(json_file):
    sample_data = [
        {"amount": 100, "category": "food"},
        {"amount": 50, "category": "transport"},
        {"amount": 200, "category": "food"}
    ]
    try:
        with open(json_file, 'w') as f:
            json.dump(sample_data, f, indent=4)
        return "Sample expenses.json created"
    except:
        return "Error: Could not create JSON file"
    

# Save the above JSON as 'expenses.json', then run:
# print(load_expenses('expenses.json'))  # [100. 50. 200.]
# print(load_expenses('expenses.json', condition=100))  # [200.]
# print(load_expenses('invalid.json'))  # Error: Invalid JSON file or data
# print(create_sample_expenses('expenses.json'))  # Sample expenses.json created
# print(load_expenses('expenses.json'))  # [100. 50. 200.]
print(load_expenses('expenses.json', stat='median'))  # 100.0
print(load_expenses('expenses.json', stat='min'))
print(load_expenses('expenses.json', stat='mean'))
print(load_expenses('expenses.json', stat='max'))

'''
Why the len(arr) == 0 Check?
Purpose: Checks if the array arr is empty (has zero elements) after filtering with arr[arr > condition].
Why It’s Needed:
If condition filters out all elements (e.g., condition=1000 on [100, 50, 200] → []), arr becomes empty.
NumPy’s np.mean, np.median, or np.min on an empty array can cause errors or return None, which caused your None results earlier.
The check stops the function early with a clear error message ("Error: No elements after filtering") instead of crashing or returning None.
Point: Ensures the function handles empty arrays safely, making your code reliable for your Expense Tracker (e.g., avoids errors when no expenses match a filter like “amount > 1000”).
'''

'''
What the amounts Line Does
The line amounts = [item['amount'] for item in data] grabs just the money values (like 100, 50, 200) from the JSON data so you can work with them in NumPy.

Simple Explanation, Line by Line
Let’s break it down like you’re brand new to coding:

What is data?
After data = json.load(f), data is a list of small dictionaries from expenses.json. Think of it like a list of notes, where each note has two pieces of info: an amount (like money spent) and a category (like what it was spent on).

What is [item['amount'] for item in data]?
This is a list comprehension, a shortcut in Python to make a new list by going through an old list.
Let’s split it:
for item in data: Loops through each “note” (dictionary) in data. So, item becomes:
First loop: {"amount": 100, "category": "food"}
Second loop: {"amount": 50, "category": "transport"}
Third loop: {"amount": 200, "category": "food"}
item['amount']: For each item (a dictionary), it grabs the value next to the key 'amount'. Think of a dictionary like a labeled box: 'amount' is the label, and 100 (or 50, 200) is what’s inside.
Example: For {"amount": 100, "category": "food"}, item['amount'] gives 100.
The [ ] part: Puts all these amount values into a new list.
Result: amounts = [100, 50, 200]
It’s like making a new list with just the money amounts, ignoring the categories.
Why Do This?
You want only the numbers (amounts) to do math with NumPy (like finding big expenses or averages).
This line pulls out the numbers from the JSON data so the next line (arr = np.array(amounts, dtype=float)) can turn them into a NumPy array for easy calculations.
'''