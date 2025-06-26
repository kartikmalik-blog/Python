import tkinter as tk

#creating main window
root = tk.Tk()
root.title("My cool app")
root.geometry("300x300")#set window size (heightxwidth)

#create a label
label = tk.Label(root, text="Hello world!", font=("Arial",18))
label.pack(pady=20) #add some padding

#validation function for character limit
def limit_characters(*args):
    max_lenght = 10
    value = entry_var.get()
    if len(value) > max_lenght:
        entry_var.set(value[:max_lenght])#Truncate the max length

#create a string Var to track the entry
entry_var = tk.StringVar()
entry = tk.Entry(root, width=20, font=("Arial", 20), textvariable=entry_var)
entry.pack(pady=10)

#Bind the validation to string var
entry_var.trace("w", limit_characters)

#creating a entry widget
entry = tk.Entry(root, width=20, font=("Arial", 20), show="*" )
entry.bind("<Return>", lambda event: update_label())
entry.pack(pady=20)

#function to change label text
def change_text():
    label.config(text="Button clicked")

#function to get entry text from user
def update_label():
    user_input = entry.get()
    if user_input:
        label.config(text=user_input.upper())
        entry.delete(0, tk.END) #clears the field
        entry.insert(0, "type here....") #default text
    else:
        label.config(text="please enter some text")

#create a button
button = tk.Button(root, text="Click me", command=change_text, bg="red", fg="black")
button.pack()

#another button to show modified input
button2 = tk.Button(root,text="show input", command=update_label, bg="black", fg="white")
button2.pack(pady=10)

#creating function to clear all
def clear_all():
    label.config(text="Hello world!")
    entry.delete(0, tk.END)


#creating another button to clear all
button = tk.Button(root, text="clear all", command=clear_all, bg="white", fg="black")
button.pack(pady=20)
#creating another function to clear var field
def clear():
    label.config(text="Hello World!")
    entry_var.set("")

#creating button to clear var field
button3 = tk.Button(root, text="clear all", command=clear, bg="Green", fg="Blue")
button3.pack(pady=20)

# #another button function
# def change_text2():
#     label.config(text="second button presed")

# #another button
# button = tk.Button(root, text="click me too", command=change_text2, bg="blue", fg="white")
# button.pack()

#start the mainloop
root.mainloop()


