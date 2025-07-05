'''
Budget Alert System
Goal: Extend analyze_expenses to compare expenses against a budget and flag over-budget categories using np.where.

What It Does:
Loads expenses.json.
Checks if expenses exceed a budget (e.g., $200 per category).
Computes stats (mean, median, max) and flags high expenses.
NumPy Skills: Arrays, filtering (np.where), stats (np.mean, np.max).
Use: Helps you monitor overspending in your Expense Tracker.
'''

import numpy as np
import json

def create_sample_expenses(json_file):
    sample_date = [
        {"amount": 100, "category":"food"},
        {"amount":200, "category":"Rent"},
        {"amount":300, "category":"semester contribution"},
        {"amount":150, "category":"entertaiment"}
    ]
    try:
        with open(json_file,'w') as f:
            json.dump(sample_date,f,indent=4)
        return "Sample expenses.json created"
    except:
        return "Error: could not create json file"
    
def budget_alert(json_file,budget=200):
    try:
        with open(json_file,'r') as f:
            data = json.load(f)
        amounts = np.array([item['amount'] for item in data],dtype=float)
        categories = [item['category'] for item in data]

        #compute expenses
        mean_expense = np.mean(amounts)
        media_expense = np.median(amounts)
        max_expense = np.max(amounts)

        #over budget
        over_budget = np.where(amounts > budget, "Over Budget", "Withing Budget")

        #Group by category
        category_sums = {}
        for amount, category in zip(amounts, categories):
            category_sums[category] = category_sums.get(category,0) + amount

        #check category budget
        category_alert  = {cat: "Over Budget" if total > budget else "Within Budget" for cat, total in category_sums.items()}

        results = {
            "mean": mean_expense,
            "median": media_expense,
            "max": max_expense,
            "over_budget_flags":list(zip(amounts, categories, over_budget)),
            "category_alert":category_alert
        }
        return results
    except(FileNotFoundError, KeyError, ValueError):
        return "Error: Invalid Json file or data"


#Run the project
if __name__ == "__main__":
    print(create_sample_expenses('expenses.json'))
    results = budget_alert('expenses.json', budget=200)
    if isinstance(results,dict):
        print(f"Mean Expense: {results['mean']:.2f}")
        print(f"Median Expense: {results['median']:.2f}")
        print(f"Max Expense: {results['max']:.2f}")
        print("Expense Alerts:", results['over_budget_flags'])
        print("Category Alerts:", results['category_alert'])
    else:
        print(results)
