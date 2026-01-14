import os

# Root of the project, relative to this file
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Data/assets folder
DATA_DIR = os.path.join(PROJECT_ROOT, "../data")

# Subfolders for convenience
SPRITES_DIR = os.path.join(DATA_DIR, "sprites")
SOUNDS_DIR = os.path.join(DATA_DIR, "sounds")
CONFIG_DIR = os.path.join(DATA_DIR, "config")
