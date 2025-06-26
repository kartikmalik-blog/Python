import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Radiobutton Example")
root.geometry("300x300")

# Create a StringVar to store the selected option
selected_option = tk.IntVar()
selected_option.set(1)  # Default selection

#create a label to display the text
label = tk.Label(root, text="Selected: Option1", font=("Arial", 14, "bold"), fg="blue")
label.grid(row=0,column=0,  columnspan=2, pady=20.)

#Function to update label when radioButton is selected
def update_label():
    # label.config(text=f"Selected: {selected_option.get()}")   
    choice = selected_option.get()
    if choice == 1:
        label.config(text="Selected: Option 1")
    elif choice == 2:
        label.config(text="Selected: Option 2")
    elif choice == 3:
        label.config(text="Selected: Option 3")
        
# Create radiobuttons
radio1 = tk.Radiobutton(root, text="Option 1", variable=selected_option, value=1, command=update_label, font=("Arial", 14, "bold"), fg="Green")
radio1.grid(row=1, column=0, padx=10, pady=10, sticky="w",)

radio2 = tk.Radiobutton(root, text="Option 2", variable=selected_option, value=2, command=update_label, font=("Arial", 14, "bold"), fg="Green")
radio2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

radio3 = tk.Radiobutton(root, text="Option 3", variable=selected_option, value=3, command=update_label, font=("Arial", 14, "bold"), fg="Green")
radio3.grid(row=3, column=0, padx=10, pady=10, sticky="w")

#Function to reset default
def reset_selection():
    selected_option.set(1)
    update_label()

#Createing reseting button
reset_button = tk.Button(root, text="Reset", command=reset_selection)
reset_button.grid(row=4, column=0, padx=10, pady=10, sticky="w")

# Start the main loop
root.mainloop()