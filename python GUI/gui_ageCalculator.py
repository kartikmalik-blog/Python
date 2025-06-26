import tkinter as tk
from datetime import datetime

#main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x300")

#Heading
label = tk.Label(root, text="Age Calculator", font=("Arial", 16))
label.pack(pady=10)

#BirthDate
day_label = tk.Label(root, text="BirthDate :")
day_label.pack()
day_entry = tk.Entry(root)
day_entry.pack()

#BirthMonth
month_label = tk.Label(root, text="BirthMonth :")
month_label.pack()
month_entry = tk.Entry()
month_entry.pack()

#BirthYear
year_label = tk.Label(root, text="BirthYear")
year_label.pack()
year_entry = tk.Entry()
year_entry.pack()

#ResultLabel
result_label = tk.Label(root, text="result", font=("Arial", 16))
result_label.pack(pady=10)

#function
def calculate_age():
    #get input
    day = day_entry.get()
    month = month_entry.get()
    year = year_entry.get()

    #check if all the fields are filled
    if day and month and year :
        try:
            #convert the input into integers
            day = int(day)
            month = int(month)
            year = int(year)

            #get today's date
            today = datetime.now()

            #create birthdate from input
            birth_date = datetime(year, month, day)

            #create age in years
            age = today.year - birth_date.year

            #Adjust age if birthday did not happen this year
            if(today.month, today.day) < (birth_date.month, birth_date.day):
                age -= 1

            #show result
            result_label.config(text=f"your age is {age} years old")

        except ValueError:
            result_label.config("Please enter the valid values")

    else:
        result_label.config("please fill all the values")

#button
calculate_button = tk.Button(root, text="CalculateAge", command=calculate_age, font=("Arial", 16), bg="White", fg="Black" )
calculate_button.pack(pady=10) 


#mainloop
root.mainloop()