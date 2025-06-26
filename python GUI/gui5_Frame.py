import tkinter as tk
from tkinter import ttk

#creat a main window
root = tk.Tk()
root.title("adding frame")
root.geometry("400x400")

#creat a var to store the value
selected_option = tk.IntVar()
selected_option.set(1) #default value

#create a var for dropdown menu
bg_color = tk.StringVar()
bg_color.set("white") #default color of background

#creat a Boolean var for check point
label_visible = tk.BooleanVar()
label_visible.set(True) #label visible by default

#Function to update label when Radio Button is selected
def update_label():
    if label_visible.get(): #only update if label is visible
        choice = selected_option.get()
        if choice == 1:
            label.config(text="Selected: Option 1")
        elif choice == 2:
            label.config(text="Selected: Option 2")
        elif choice == 3:
            label.config(text="Selected Option 3")
    else:
        label.config("") #clear label if empty


#Function to change the background color
def change_bg(*args):
    # root.configure(bg=bg_color.get()) 
    selected_color = bg_color.get()
    #update background color of all relevant widgets
    color_label.configure(bg=selected_color)
    radio1.configure(bg=selected_color)
    radio2.configure(bg=selected_color)
    radio3.configure(bg=selected_color)
    toggle_check.configure(bg=selected_color)

#Function to toggle label visiblity
def toggle_label():
    if label_visible.get():
        label.grid(row=0, column=0, columnspan=2, pady=20)
        update_label()
    else:
        label.grid_remove() #hide the label

#create a frame to organise the widgets
frame = tk.Frame(root, bg="white", padx=10, pady=10)
frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

#create a label to display the stored value
label = tk.Label(root, text="Selected: Option 1", font=("Arial", 14, "bold"), fg="blue", bg="white")
label.grid(row=0, column=0, columnspan=2, pady=20)

#create radioButton inside the frame
radio1 = tk.Radiobutton(frame, text="Option 1", variable=selected_option, value=1, command=update_label, font=("Arial", 14, "bold"), fg="Green", bg="white")
radio1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

radio2 = tk.Radiobutton(frame, text="Optiom 2", variable=selected_option, value=2, command=update_label, font=("Arial", 14, "bold"), fg="Green", bg="white" )
radio2.grid(row=1, column=0, padx=10, pady=10, sticky="w")

radio3 = tk.Radiobutton(frame, text="Option 3", variable=selected_option, value=3, command=update_label, font=("Arial", 14, "bold"), fg="Green", bg="white")
radio3.grid(row=2, column=0, padx=10, pady=10, sticky="w")

#create a drop down menu for background color
color_label = tk.Label(frame, text="Choose Background:", font=("Aria", 12), bg="white")
color_label.grid(row=3, column=0, padx=10, pady=10, sticky="w" )

color_dropdown = ttk.Combobox(frame, textvariable=bg_color, values=["lightgray", "lightgreen", "blue", "white", "lightpink"], state="readonly")
color_dropdown.grid(row=4, column=0, padx=10, pady=10, sticky="w")
color_dropdown.bind("<<ComboboxSelected>>", change_bg)

#create a check button to toggle the visiblity
toggle_check = tk.Checkbutton(frame, text="Show Label", variable=label_visible, command=toggle_label, font=("Arial", 13), bg="white")
toggle_check.grid(row=5, column=0, padx=10, pady=10, sticky="w")

#Function to reset default
def reset():
    selected_option.set(1)
    bg_color.set("white")
    label_visible.set(True)
    root.configure(bg="white")
    label.configure(bg="white")
    frame.configure(bg="white")
    color_label.configure(bg="white")
    radio1.configure(bg="white")
    radio2.configure(bg="white")
    radio3.configure(bg="white")
    toggle_check.configure(bg="white")
    toggle_label()
    update_label()

#create a button to reset
reset_button = tk.Button(frame, text="Reset", command=reset, font=("Aria", 12))
reset_button.grid(row=6, column=0, padx=10,pady=10, sticky="w")

#create a mainloop
root.mainloop()




