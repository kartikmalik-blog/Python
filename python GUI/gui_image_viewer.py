import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

#main window
root = tk.Tk()
root.title("image viewer")
root.geometry("300x300")

#function to open and show image
def open_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
)

    if file_path:
        image = Image.open(file_path)
        image = image.resize((400,400))
        photo = ImageTk.PhotoImage(image)

        label.config(image=photo)
        label.image = photo

#button to open image
open_image = tk.Button(root, text="open image", command=open_image, font=("Arial", 19))
open_image.pack(pady=10)

#label to display image
label = tk.Label(root)
label.pack(pady=10)

#start the mainloop
root.mainloop()
