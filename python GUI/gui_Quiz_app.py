import tkinter as tk

# Main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("400x300")

# Questions data (4 options per question)
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Milan", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Earth", "Venus", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote 'A Song of Ice and Fire'?",
        "options": ["J.K. Rowling", "George R.R. Martin", "Tolkien", "C.S. Lewis"],
        "answer": "George R.R. Martin"
    }
]

# Track question number and score
question_index = 0
score = 0

# Variable to store selected answer
selected_option = tk.StringVar()

# Layout frames
question_frame = tk.Frame(root)
question_frame.pack(pady=20)

option_frame = tk.Frame(root)
option_frame.pack()

# Question label
question_label = tk.Label(question_frame, text="", wraplength=350, font=("Arial", 12))
question_label.pack()

# Radiobuttons for options
option_buttons = []
for i in range(4):
    btn = tk.Radiobutton(option_frame, text="", variable=selected_option, value="", font=("Arial", 10))
    btn.pack(anchor="w")
    option_buttons.append(btn)

#load questions
def load_question():
    global question_index
    question = questions[question_index]
    question_label.config(text=question["question"])
    selected_option.set(None) #deselect any previous options

    for i,option in enumerate(question["options"]):
        option_buttons[i].config(text=option, value=option )

#Handle next question
def next_question():
    global question_index, score

    selected = selected_option.get()
    if selected == "":
        return  #no options selected
    
    if selected == questions[question_index]["options"]:
        score +=1

    question_index += 1

    if question_index < len(questions):
        load_question()
    else:
        show_results()

#show final score
def show_results():
    question_label.config(text=f"you scored {score} out of {len(questions)}")
    for btn in option_buttons:
        btn.pack_forget()
    next_button.pack_foget()

#next button
next_button = tk.Button(root, text="Next", command=next_question, font=("Aria", 19))
next_button.pack(pady=10)


# Main loop
load_question()
root.mainloop()
