import tkinter as tk
from tkinter import messagebox
import datetime
import time 
import pygame
import os 

#initialize sound
pygame.mixer.init()

# Load tick sound safely
alarm_path = os.path.join(os.path.dirname(__file__), "alarm.wav")
alarm_sound = pygame.mixer.Sound(alarm_path)

#main window
root = tk.Tk()
root.title("Alaram Clock")
root.geometry("300x250")
root.configure(bg="#222")

#Heading
heading_label = tk.Label(root, text="Alarm Clock", font=("Arial", 16),fg="White", bg="#222")
heading_label.pack(pady=10)

#TimeLabel
time_label = tk.Label(root, text="Enter Time (HH:MM AM/PM)",font=("Aria", 12), fg="lightblue", bg="#222")
time_label.pack(pady=10)

#Entry box
alarm_time = tk.Entry(root, font=("Arial", 12), justify="center")
alarm_time.pack(pady=10)

#function to check the alaram
def check_alarm():
    current_time = time.strftime("%I:%M %p")
    entered_time = alarm_time.get().strip()

    if entered_time == current_time:
        pygame.mixer.Sound.play(alarm_sound)
        messagebox.showinfo("Alarm: Time to wake up")
    root.after(1000, check_alarm)

#start button
start_alarm = tk.Button(root, text="Start", command=check_alarm, font=("Arial",12), bg="White", fg="black")
start_alarm.pack(pady=20)

#mainloop
root.mainloop()


