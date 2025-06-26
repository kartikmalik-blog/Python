import tkinter as tk
from tkinter import ttk, filedialog

root = tk.Tk()
root.title("My Cool App")
root.geometry("300x300")

# Create a frame
frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

# Label in frame
label = tk.Label(frame, text="Hello World!", font=("Arial", 18))
label.grid(row=0, column=0, columnspan=2, pady=10)

#check button
bold_var = tk.BooleanVar()
check = ttk.Checkbutton(root, text="Bold text", variable=bold_var, command=lambda: label.config(font=("Arial", 18, "bold" if bold_var.get() else "")))
check.grid(pady=10)

# Function for "Save" command
def save():
    text = entry.get()
    if text:
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file:
            with open(file, "w") as f:
                f.write(text)
            label.config(text="Saved!")
    else:
        label.config(text="Enter text to save!")

# Function for "Open" command
def open_file():
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file:
        with open(file, "r") as f:
            text = f.read()
            entry.delete(0, tk.END)
            entry.insert(0, text)
        label.config(text="File Opened!")

# Function for "Clear" command
def clear():
    entry.delete(0, tk.END)
    label.config(text="Cleared!")

#Menu
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
file_menu.add_command(label="save", command=save)
file_menu.add_command(label="open", command=open_file)
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_separator()
file_menu.add_command(label="clear", command=clear)
root.config(menu=menubar)

# Entry with StringVar
entry_var = tk.StringVar()
entry = ttk.Entry(frame, width=20, font=("Arial", 14), textvariable=entry_var)
entry.grid(row=1, column=0, columnspan=2, pady=10)

# Validation
def limit_characters(*args):
    max_length = 10
    value = entry_var.get()
    if len(value) > max_length:
        entry_var.set(value[:max_length])

entry_var.trace("w", limit_characters)

# Buttons in grid
button1 = ttk.Button(frame, text="Click Me", command=lambda: label.config(text="Button clicked"))
button1.grid(row=2, column=0, padx=5, pady=5)
button2 = ttk.Button(frame, text="Show Input", command=lambda: label.config(text=entry_var.get().upper()))
button2.grid(row=2, column=1, padx=5, pady=5)

# Clear button
button_clear = ttk.Button(frame, text="Clear All", command=lambda: [label.config(text="Hello World!"), entry.delete(0, tk.END)])
button_clear.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()

