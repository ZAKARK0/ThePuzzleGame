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


            elapsed_time = time.time() - self.start_time
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

            # Append name and time to leaderboard file
            with open("static/leaderboard.txt", "a") as file:
                file.write(f"{name}: {time_str}\n")

            # Show finish message with recorded time
            messagebox.showinfo("Finish", f"Timer stopped. Time recorded for {name}: {time_str}")

    def update_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.time_label.config(text=time_str)
            self.root.after(1000, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
