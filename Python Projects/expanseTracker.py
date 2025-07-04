import numpy as np
import json

def create_sample_expanses(json_file):
    sample_data = [
        {"amount":100, "category":"food"},
        {"amount":200, "category":"Transport"},
        {"amount":300, "category":"Rent"},
        {"amount":400,"category":"Semester Contribution"}
    ]
    try:
        with open(json_file,'w') as f:
            json.dump(sample_data, f, indent=4)
            return "Sample expanses.json created"
    except:
        return "Error: could not file expanses.json"
    
def load_expanses(json_file, condition=None, stat=None):
    try:
        with open(json_file,'r') as f:
            data = json.load(f)
        amounts = [item['amount'] for item in data]
        arr = np.array(amounts,dtype=float)
        if condition is not None:
            arr = arr[arr>condition]
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
    except(FileNotFoundError, KeyError, ValueError,TypeError):
        return "Error: Invalid Json file or data"

def analyze_expenses(json_file, threshold=100):
    try:
        with open(json_file,'r') as f:
            data = json.load(f)
        amounts = np.array([item['amount'] for item in data], dtype=float)
        categories = [item['category'] for item in data]

        #compute_stats
        mean_expenses = np.mean(amounts)
        median_expenses = np.median(amounts)
        min_expenses = np.min(amounts)
        max_expenses = np.max(amounts)

        #Filter high low expenses
        high_expenses = amounts[amounts > threshold]
        low_expenses = amounts[amounts <= threshold]

        #Group by category
        category_sums = {}
        for amount, category in zip(amounts,categories):
            category_sums[category] = category_sums.get(category,0) + amount
        
        #Return Result
        results = {
            "mean": mean_expenses,
            "median": median_expenses,
            "min": min_expenses,
            "max": max_expenses,
            "high_expenses": high_expenses,
            "low_expenses": low_expenses,
            "category_sums": category_sums
        }
        return results
    except(FileNotFoundError, KeyError, ValueError):
        return "Error: invalid json file or data"
    
#Run the project
if __name__ == "__main__":
    #create sample data
    print(create_sample_expanses('expenses.json'))

    #Run basic analysis
    print("Basic Analysis:")
    print("All expneses:", load_expanses('expenses.json'))
    print("Expenses > 100:", load_expanses('expenses.json', condition=100))
    print("mean:", load_expanses('expenses.json', stat='mean'))
    print("media:", load_expanses('expenses.json', stat='median'))
    print("min:", load_expanses('expenses.json', stat='min'))
    print("max:", load_expanses('expenses.json', stat='max'))


    #Run detailed analysis
    print("\nDetailed Analysis:")
    results = analyze_expenses('expenses.json',threshold=100)
    if isinstance(results,dict):
        print(f"mean Expense: {results['mean']:.2f}")
        print(f"median Expense: {results['median']:.2f}")
        print(f"min Expense: {results['min']:.2f}")
        print(f"max Expense: {results['max']:.2f}")
        print("High Expense: (>100):", results['high_expenses'])
        print("low Expenses (<=100):", results['low_expenses'])
        print("Category Totals:", results['category_sums'])
    else:
        print(results)


