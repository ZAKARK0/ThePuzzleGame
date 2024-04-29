import tkinter as tk
from tkinter import messagebox
import time
class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")
        self.root.geometry("300x200")

        # Label to inform the user to start the game first
        self.info_label = tk.Label(self.root, text="Start the game before starting the timer")
        self.info_label.pack(pady=(20, 5))

        # Label and Entry for user to input their name
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.pack(pady=(20, 5))
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        # Label to display the timer
        self.time_label = tk.Label(self.root, text="00:00:00", font=("Arial", 24))
        self.time_label.pack(pady=10)

        # Button to start/finish the timer
        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.timer_running = False
        self.start_time = None
    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_time = time.time()
            self.update_timer()
            self.start_button.config(text="Finish", command=self.finish_timer)
        else:
            messagebox.showinfo("Timer", "Timer already running!")

    def finish_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.start_button.config(text="Start", command=self.start_timer)

            name = self.name_entry.get().strip()  # Get the name from the entry box
            if not name:
                messagebox.showwarning("Warning", "Please enter a name!")
                return