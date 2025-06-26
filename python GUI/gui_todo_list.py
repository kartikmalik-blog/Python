import tkinter as tk

#create a main window
root = tk.Tk()
root.title("todo List")
root.geometry("300x300")

#create entry to get the input 
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

#List to store values
todoList = []

#Function to add task
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        todoList.append(task)
        entry.delete(0, tk.END)

#Function to remove task
def remove_task():
    selected = listbox.curselection()
    if selected:
        task_index = selected[0]
        listbox.delete(task_index)
        todoList.pop(task_index)

#add task button
add_button = tk.Button(root, text="add task", command=add_task, font=("Arial", 10))
add_button.pack(pady=10)

#listbox to show 
listbox = tk.Listbox(root, font=("Aria", 19), width=30, height=10 )
listbox.pack(pady=5)

#button to remove 
remove_button = tk.Button(root, text="Remove task", command=remove_task, font=("Arial", 19))
remove_button.pack(pady=10)

#start the mainloop
root.mainloop()