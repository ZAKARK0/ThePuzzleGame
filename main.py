import pygame
import random
import os
from PIL import Image
import subprocess
# Initialize Pygames
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800  # Adjusted height to fit 10x10 grid
GRID_SIZE = 10  # Size of the invisible grid
IMAGE_SIZE = 80  # Size of each image
PIECE_FOLDER = "pieces100"  # Updated folder name
NUM_IMAGES = 100


# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Load and Resize Images
pieces = []
for i in range(NUM_IMAGES):
    image_path = os.path.join(PIECE_FOLDER, f"{i}.jpg")
    image = Image.open(image_path)
    image = image.resize((IMAGE_SIZE, IMAGE_SIZE), resample=Image.LANCZOS)
    pieces.append(pygame.image.frombuffer(image.tobytes(), image.size, image.mode))

# Initialize Game Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Puzzle Game")

clock = pygame.time.Clock()

# Initialize Pygame mixer
pygame.mixer.init()

# Load the music file
music_file = os.path.join("static", "music.mp3")
pygame.mixer.music.load(music_file)

# Set the initial state for the music player
music_playing = True
pygame.mixer.music.play(-1)  # -1 means loop indefinitely

# Load and resize the music button images
mute_button_image = pygame.image.load(os.path.join("static", "mute.png"))
mute_button_image = pygame.transform.scale(mute_button_image, (30, 30))
unmute_button_image = pygame.image.load(os.path.join("static", "unmute.png"))
unmute_button_image = pygame.transform.scale(unmute_button_image, (30, 30))
music_button_image = unmute_button_image
music_button_rect = music_button_image.get_rect(topleft=(10, 10))
