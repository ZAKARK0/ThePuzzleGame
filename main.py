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
