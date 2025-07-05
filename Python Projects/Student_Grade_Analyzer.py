import numpy as np
import json
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Save grades to JSON
def save_grades(json_file, grades):
    try:
        data = [{"grades": g} for g in grades]
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)
        return "Grades saved in the JSON file"
    except:
        return "Error: Could not save grades"

# Load and analyze grades
def analyze_grades(json_file, pass_threshold=60):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        grades = np.array([item['grades'] for item in data], dtype=float)

        # Compute grades
        mean_grade = np.mean(grades)
        median_grade = np.median(grades)
        max_grade = np.max(grades)
        min_grade = np.min(grades)

        # Filter pass or fail
        pass_grades = grades[grades >= pass_threshold]
        fail_grades = grades[grades < pass_threshold]

        results = {
            "mean": mean_grade,
            "median": median_grade,
            "max": max_grade,
            "min": min_grade,
            "pass_count": len(pass_grades),
            "fail_count": len(fail_grades)
        }
        return results
    except (FileNotFoundError, KeyError, ValueError):
        return "Error: Invalid JSON file"

# CUI to collect grades
def collect_grades():
    grades = []
    print("Enter the grades from (0-100). Type 'done' to finish\n")
    while True:
        user_input = input("Grades: ")
        if user_input.lower() == 'done':
            break
        try:
            grade = float(user_input)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Grades must be between 0 to 100")
        except ValueError:
            print("Invalid Error: please enter a number or 'done'")
    if grades:
        print(save_grades('grades.json', grades))
    return grades

# GUI to display results
class GradeAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grade Analyzer")
        
        # Buttons
        tk.Button(root, text="Collect Grades (CUI)", command=self.run_cui).pack(pady=5)
        tk.Button(root, text="Analyze Grades", command=self.show_results).pack(pady=5)
        
        # Result display
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=5)
        
        # Plot area
        self.fig, self.ax = plt.subplots(figsize=(4, 3))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()

    def run_cui(self):
        collect_grades()
        messagebox.showinfo("Success", "Grades Collected. Click 'Analyze Grades' to see results.")

    def show_results(self):
        results = analyze_grades('grades.json')
        if isinstance(results, dict):
            # Update label
            result_text = (f"Mean: {results['mean']:.2f}\n"
                          f"Median: {results['median']:.2f}\n"
                          f"Min: {results['min']:.2f}\n"
                          f"Max: {results['max']:.2f}\n"
                          f"Pass (≥60): {results['pass_count']}\n"
                          f"Fail (<60): {results['fail_count']}")
            self.result_label.config(text=result_text)

            # Plot bar chart
            self.ax.clear()
            self.ax.bar(['Pass', 'Fail'], [results['pass_count'], results['fail_count']], color=['green', 'red'])
            self.ax.set_ylabel("Number of Students")
            self.ax.set_title("Pass/Fail Distribution")
            self.canvas.draw()
        else:
            messagebox.showerror("Error", results)

# Run the project
if __name__ == "__main__":
    # Start with CUI to collect grades
    print("Starting Grade Analyzer...")
    collect_grades()
    
    # Launch GUI
    root = tk.Tk()
    app = GradeAnalyzerGUI(root)
    root.mainloop()