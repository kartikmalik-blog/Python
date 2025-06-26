import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.config(bg="#2c3e50")

entry = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

def click(btn_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + btn_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error: Invalid number:")

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('+',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('-',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('*',3,3),
    ('C',4,0), ('0',4,1), ('=',4,2), ('/',4,3),
]

for(text,row,col) in buttons:
    if text == "=":
        action = calculate
    elif text == "c":
        action = clear
    else:
        action = lambda x=text: click(x)

    tk.Button(root, text=text, padx=20, font=("Arial",14), bg="#ecf0f1", command=action).grid(row=row, column=col, sticky="nsew")

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1) 


root.mainloop()