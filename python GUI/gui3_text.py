import tkinter as tk
from tkinter import ttk,  filedialog

#creating main window
root = tk.Tk()
root.title("Text widget expierencer")
root.geometry("300x300")

#frame to hold both 
frame = tk.Frame(root)
frame.pack(pady=10, fill="both", expand=True)

#creating text widget:-
text_widget = tk.Text(frame, wrap="word", font=("Arial", 12))
text_widget.pack(side="left", fill="both", expand=True)

#creating scroll bar:-
scroll_bar = tk.Scrollbar(frame, orient="vertical", command=text_widget.yview)
scroll_bar.pack(side="right", fill="y")

#Linking scrollbar to textwidget:-
text_widget.configure(yscrollcommand=scroll_bar.set)

#creating label to count characters and words:-
counter_label = tk.Label(root, text="Characters: 0 | words: 0", font=("Arial", 10))
counter_label.pack()

#--counter update function--
def update_counter(event=None):
    text = text_widget.get("1.0", "end-1c") #get text, exclude last new line
    char_count = len(text)
    word_count = len(text.split())
    counter_label.config(text=f"Characters: {char_count} | words: {word_count}")

    text_widget.edit_modified(False) #Resest modified flag so it resets again

#Bind counter to text modification
text_widget.bind("<<Modified>>", update_counter)


#Buttons Functions:-
def save_text():
    # 1. Get the text from the Text widget
    content = text_widget.get("1.0", "end-1c")  
    # "1.0" means starting at line 1, character 0 (the very beginning)
    # "end-1c" means up to the very end minus 1 character (to avoid the automatic newline Tkinter adds)

    # 2. Open a Save As dialog and ask user where to save the file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",  # If user doesn't add extension, add .txt automatically
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]  
        # Filters for file types shown in the dialog
    )

    # 3. If user selects a file and doesn't cancel
    if file_path:  
        # Open the file in write mode ("w"), with utf-8 encoding to support all characters
        with open(file_path, "w", encoding="utf-8") as file:  
            file.write(content)  # Write the text content into that file

        # 4. Optional: update the label to show feedback
        counter_label.config(text="File saved!")  

def open_text():
    file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file:
        with open(file, "r") as file:
            content = file.read()
            text_widget.delete("1.0", tk.END)
            text_widget.insert("1.0", content)
        update_counter()


def clear():
    text_widget.delete("1.0", tk.END)
    update_counter()

#Function to search and highlight all the matches of the "term" in the text widget:-
def search_text(term):
    #Remove any previous highlighted by deleting "highlight" tag from entry
    text_widget.tag_remove("highlight","1.0", tk.END)

    #if search term is not empty:-
    if term:
        start_pos = "1.0" #start searching from the very begining

        while True:
            #search for the 'term' from the start pos to end
            # nocase=1 means case insensitive search
            start_pos = text_widget.search(term, start_pos, nocase=1, stopindex=tk.END)

            if not start_pos: #if no more matches found exit loop
                break

            #calculate the end position of the match by adding the length of "term" to start_pos
            end_pos = f"{start_pos}+{len(term)}c"

            #Add a tag called "highlight" to the matched text range(start_pos and end_pos)
            text_widget.tag_add("highlight", start_pos, end_pos)

            #move the start_pos forward past this match  to keep searching the rest of the text
            start_pos = end_pos

        #configure how the "highlighter" tag looked:
        text_widget.tag_config('highlight', background='yellow')


search_var = tk.StringVar() #create a string variable to store input

#entry widget for input
search_entry = ttk.Entry(root, textvariable=search_var, width=20)
search_entry.pack(pady=5) #add some spacing

#Button that will calls the search entry by user:-
search_button = tk.Button(root, text="search",command=lambda: search_text(search_var.get()))
search_button.pack()


#Adding buttons:-
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Save", command=save_text).pack(side="left", padx=5)
tk.Button(button_frame, text="open", command=open_text).pack(side="left", padx=5)
tk.Button(button_frame, text="clear", command=clear).pack(side="left", padx=5)

root.mainloop()
