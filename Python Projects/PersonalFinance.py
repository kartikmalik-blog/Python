import tkinter as tk
from tkinter import messagebox
import json
import os

# List to store expenses
expenses = []

# Function to validate and add expense
def add_expense(amount, category, description, date):
    if not (isinstance(amount, (int, float)) and amount > 0):
        return "Error: Amount must be a positive number"
    if not isinstance(category, str) or not category.strip():
        return "Error: Category must be a non-empty string"
    if not isinstance(description, str):
        return "Error: Description must be a string"
    if not isinstance(date, str) or not date.strip():
        return "Error: Date must be a non-empty string"
    
    expense = {"amount": amount, "category": category, "description": description, "date": date}
    expenses.append(expense)
    result = save_expenses_to_file()
    if "Error" in result:
        return f"Expense added but failed to save: {result}"
    return "Expense added successfully"

# Function to save expenses to JSON file with error handling and optional filename
def save_expenses_to_file(**kwargs):
    filename = kwargs.get("filename", "expenses.json")
    if not expenses:
        return "Error: No expenses to save"
    try:
        with open(filename, "w") as file:
            json.dump(expenses, file, indent=4)
        return "Saved successfully"
    except (IOError, PermissionError) as e:
        return f"Error: Failed to save file - {str(e)}"

# GUI setup
def create_gui():
    window = tk.Tk()
    window.title("Personal Finance Tracker")
    window.geometry("400x300")

    # Label and Entry fields
    tk.Label(window, text="Amount:").grid(row=0, column=0, padx=10, pady=5)
    amount_entry = tk.Entry(window)
    amount_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(window, text="Category:").grid(row=1, column=0, padx=10, pady=5)
    category_entry = tk.Entry(window)
    category_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(window, text="Description:").grid(row=2, column=0, padx=10, pady=5)
    description_entry = tk.Entry(window)
    description_entry.grid(row=2, column=1, pady=10, padx=5)

    tk.Label(window, text="Date (YYYY-MM-DD):").grid(row=3, column=0, pady=10, padx=5)
    date_entry = tk.Entry(window)
    date_entry.grid(row=3, column=1, pady=10, padx=5)

    # Button callback function
    def submit_expense():
        try:
            amount = float(amount_entry.get())
            category = category_entry.get()
            description = description_entry.get()
            date = date_entry.get()
            result = add_expense(amount, category, description, date)
            messagebox.showinfo("Result", result)
            if "success" in result.lower():
                amount_entry.delete(0, tk.END)
                category_entry.delete(0, tk.END)
                description_entry.delete(0, tk.END)
                date_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number")

    # Button to add expense
    tk.Button(window, text="Add Expense", command=submit_expense).grid(row=4, column=0, columnspan=2, pady=10)

    window.mainloop()

# Load expenses from file (if exists)
def load_expenses(**kwargs):
    global expenses
    filename = kwargs.get("filename", "expenses.json")
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                expenses = json.load(file)
            return "Loaded successfully"
        except (IOError, json.JSONDecodeError) as e:
            return f"Error: Failed to load file - {str(e)}"
    return "No file found, starting with empty expenses"

# Run the app
if __name__ == "__main__":
    print(load_expenses())  # Debug print to check loading
    create_gui()