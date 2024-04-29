import tkinter as tk
class LeaderboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Leaderboard")
        self.root.geometry("400x300")

        # Configure styles for the root window
        self.root.configure(bg="black")  # Set the window background to black

        # Create and configure the leaderboard label
        self.leaderboard_label = tk.Label(self.root, text="Leaderboard", font=("Arial", 18, "bold"), fg="white", bg="black")
        self.leaderboard_label.pack(pady=(10, 5))  # Add padding to the label

        # Create and configure the leaderboard listbox
        self.leaderboard_listbox = tk.Listbox(self.root, width=50, height=10, font=("Arial", 12, "bold"), fg="white", bg="black")
        self.leaderboard_listbox.pack(pady=10)  # Add padding to the listbox

        # Call the update_leaderboard method to populate the listbox
        self.update_leaderboard()

    def update_leaderboard(self):
        # Clear the existing items in the listbox
        self.leaderboard_listbox.delete(0, tk.END)

        # Read the leaderboard data from the file
        with open("static/leaderboard.txt", "r") as file:
            lines = file.readlines()
            entries = []
            for line in lines:
                # Parse each line to extract name and time
                name, time_str = line.strip().split(": ")
                entries.append((name, time_str))