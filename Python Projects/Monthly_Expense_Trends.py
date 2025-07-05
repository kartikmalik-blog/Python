'''
Monthly Expense Trends
Goal: Analyze expenses from multiple JSON files (e.g., monthly data) to compute month-over-month changes using np.diff.

What It Does:
Loads two JSON files (e.g., January, February expenses).
Computes total expenses per month and differences.
Identifies biggest changes.
NumPy Skills: Arrays, concatenation (np.concatenate), differences (np.diff).
Use: Tracks spending trends for your Expense Tracker.
'''

import numpy as np
import json

def create_monthly_expenses(json_file1, json_file2):
    month1_data = [
        {"amount":100, "category":"food"},
        {"amount":200, "category":"transport"}
    ]
    month2_data = [
        {"amount":120, "category":"food"},
        {"amount":100, "category":"transport"}
    ]
    try:
        with open(json_file1,'w') as f:
            json.dump(month1_data,f,indent=4)
        with open(json_file2,'w') as f:
            json.dump(month2_data,f,indent=4)
        return "Monthly Expense trends created"
    except:
        return "Error: could not be able to create json files"
    
def expense_trends(json_file1, json_file2):
    try:
        with open(json_file1, 'r') as f:
            month1 = json.load(f)
        with open(json_file2, 'r') as f:
            month2 = json.load(f)
        
        amounts1 = np.array([item['amount'] for item in month1], dtype=float)
        amounts2 = np.array([item['amount'] for item in month2], dtype=float)
        
        # Total expenses per month
        total1 = np.sum(amounts1)
        total2 = np.sum(amounts2)
        
        # Month-over-month difference
        totals = np.array([total1, total2])
        diff = np.diff(totals)[0]
        
        results = {
            "month1_total": total1,
            "month2_total": total2,
            "difference": diff,
            "change": "Increase" if diff > 0 else "Decrease" if diff < 0 else "No Change"
        }
        return results
    except (FileNotFoundError, KeyError, ValueError):
        return "Error: Invalid JSON file or data"
    
        
#Run the project
if __name__ == "__main__":
    print(create_monthly_expenses('jan_expenses.json', 'feb_expenses.json'))
    results = expense_trends('jan_expenses.json','feb_expenses.json')
    if isinstance(results,dict):
        print(f"January Total: {results['month1_total']:.2f}")
        print(f"February Total: {results['month2_total']:.2f}")
        print(f"Difference: {results['difference']:.2f}")
        print("Change:", results['change'])
    else:
        print(results)


