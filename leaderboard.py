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

            # Sort the entries based on time (using time_to_seconds function)
            sorted_entries = sorted(entries, key=lambda x: self.time_to_seconds(x[1]))

            # Display the sorted entries in the listbox
            for idx, (name, time_str) in enumerate(sorted_entries, start=1):
                self.leaderboard_listbox.insert(tk.END, f"{idx}. {name}: {time_str}")

        # Schedule the update_leaderboard method to run again after 1000ms (1 seond)
        self.root.after(1000, self.update_leaderboard)

    def time_to_seconds(self, time_str):
        # Convert time string (HH:MM:SS) to seconds for sorting
        hours, minutes, seconds = map(int, time_str.split(":"))
        return hours * 3600 + minutes * 60 + seconds

if __name__ == "__main__":
    root = tk.Tk()  # Create the Tkinter root window
    app = LeaderboardApp(root)  # Create an instance of the LeaderboardApp class
    root.mainloop()  # Start the Tkinter event loop
