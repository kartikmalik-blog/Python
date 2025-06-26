import tkinter as tk

# Main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

# Heading Label
heading = tk.Label(root, text="BMI Calculator", font=("Arial", 16))
heading.pack(pady=10)

# Weight
weight_label = tk.Label(root, text="Enter Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

# Height
height_label = tk.Label(root, text="Enter Height (cm):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

#BMI Calculate
def Calculate_bmi():

    #Get values into input
    weight = weight_entry.get()
    height = height_entry.get()

    #Make sure both entries are filled
    if weight and height:
        try:
            weight = float(weight)
            height = float(height)/100 #converts into m

            bmi = weight / (height ** 2)
            bmi = round(bmi, 2)

            #if categorize bmi
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 25:
                category = "Normalweight"
            elif 25 <= bmi <30:
                category = "Overweight"
            else:
                category = "Obese"

            #show result
            result_label.config(text=f"BMI: {bmi} ({category})")
            print("DEBUF: BMI", bmi)


        except ValueError:
            result_label.config(text="Please enter the valid number")

    else:
        result_label.config(text="please fill both fields")

#clear
def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")

#button
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

calculate_button = tk.Button(button_frame, text="Calculate BMI", command=Calculate_bmi, font=("Arial", 11), bg="#4CAF50", fg="white", padx=10, pady=5)
calculate_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_fields, font=("Arial", 11), bg="#f44336", fg="white", padx=10, pady=5)
clear_button.pack(side=tk.LEFT, padx=10)

# Start the app
root.mainloop()
