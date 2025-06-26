import tkinter as tk
import time
import pygame 
import os 

# Initialize pygame mixer for playing ticking sound
pygame.mixer.init()

# Load tick sound safely
tick_path = os.path.join(os.path.dirname(__file__), "tick.wav")
tick_sound = pygame.mixer.Sound(tick_path)

#main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x150")
root.configure(bg="#1a1a1a") 

#clock frame to simulate digital clock
clock_frame = tk.Frame(root, bg="#000000", bd=10, relief="ridge")
clock_frame.pack(pady=30, padx=30)

# Time Label (inside the frame)
time_label = tk.Label(clock_frame, text="", font=("DS-Digital", 50), fg="#00FF99", bg="#000000")
time_label.pack()

# AM/PM Label
ampm_label = tk.Label(clock_frame, text="", font=("Arial", 16), fg="white", bg="#000000")
ampm_label.pack()

# Date Label (below frame)
date_label = tk.Label(root, text="", font=("Arial", 14), fg="yellow", bg="#1a1a1a")
date_label.pack(pady=10)

#function to update time
def update_clock():
    current_time = time.strftime("%I:%M:%S")   # 12-hour format with leading 0
    am_pm = time.strftime("%p")                # AM or PM
    today_date = time.strftime("%A, %d %B %Y") # Example: Monday, 17 June 2025

    time_label.config(text=current_time)
    ampm_label.config(text=am_pm)
    date_label.config(text=today_date)

    # Play tick sound
    # winsound.Beep(1000, 100)  # (frequency in Hz, duration in ms)
    tick_sound.play()  # play tick every second

    root.after(1000, update_clock)
#mainloop
update_clock()
root.mainloop()