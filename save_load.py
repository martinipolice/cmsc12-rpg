# save_load.py

import json
import os

SAVE_FILE = "game.save"

def save_game(player):
    """Save current player data into a file."""
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(player, f, indent=4)
        print("\nProgress saved successfully.")
    except Exception as e:
        print(f"Error saving game: {e}")


def load_game():
    """Load player data from a save file."""
    if not os.path.exists(SAVE_FILE):
        print("\nNo save file found.")
        return None

    try:
        with open(SAVE_FILE, "r") as f:
            player = json.load(f)
        print("\nGame loaded successfully.")
        return player
    except Exception as e:
        print(f"Error loading game: {e}")
        return None
