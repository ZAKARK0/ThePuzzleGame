
<!-- Puzzle Game Project -->

Link to my repository:
https://github.com/ZAKARK0/ThePuzzleGame
## Overview
This project is a puzzle game implemented in Python using the Pygame library. 
It allows players to solve puzzles by arranging shuffled pieces to form a complete image.
the project also runs 2 additional programs , both use file handling and datetime and one
uses sorting algorithm
which is the leaderboard algorithm that sorts the players based on time
timers deals with user input and error handling if the input is empty
the main function has all sorts of functionalities and file handling methods

## Installation
1. Clone the repository to your local machine:
   ```
   git clone https://github.com/ZAKARK0/ThePuzzleGame.git
   

Navigate to the project directory:
cd puzzle-game

Install the required dependencies using pip:
pip install -r requirements.txt


Usage
Run the main game script:
python main_game.py
Follow the on-screen instructions to start the game and solve the puzzle.
Additionally, you can run the timer and leaderboard apps as separate processes:
python timer.py
python leaderboard.py
Dependencies
pygame (version 2.0.1): Used for game development.
pip install pygame==2.0.1

Pillow (version 8.4.0): Provides image processing capabilities.
pip install Pillow==8.4.0

tkinter (version 8.6): GUI toolkit included in Python's standard library.

Optional Dependencies
numpy (version 1.21.5): Used for numerical operations if needed.
pip install numpy==1.21.5

File Structure
main_game.py: Contains the main game logic and GUI using Pygame.
timer.py: Implements a timer app using tkinter for recording game completion times.
leaderboard.py: Displays a leaderboard using tkinter to show player scores.
static: contains the music mp3 file and the images used to animate the mute and unmute button , and leaderboard.txt that acts as a database for the leaderboard

Contributing
Fork the repository and clone it to your local machine.
Create a new branch for your feature or bug fix:

git checkout -b feature/your-feature-name
Make your changes and test them thoroughly.
Commit your changes:

git commit -am "Add your commit message here"

Push to your branch:
git push origin feature/your-feature-name
Create a new Pull Request on GitHub.
License
This project is licensed under the MIT License. See the LICENSE file for details.





