# save_load.py

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_FILE = os.path.join(BASE_DIR, "game.save")

def save_game(player):
    try:
        # Always use context manager; ensures close + flush
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            # Line 1: core stats
            f.write(f"{player['Name']}|{player['HP']}|{player['maxHP']}|")
            f.write(f"{player['ATK']}|{player['DEF']}|{player['SPD']}|")
            f.write(f"{player['Gold']}|{player['Day']}\n")
            # Line 2: potions
            f.write(f"{player['Potion']['Small']}|{player['Potion']['Big']}|{player['Potion']['Panacea']}\n")
        print("\nProgress saved successfully.")
        verify_save()
    except Exception as e:
        print(f"Error saving game: {e}")

def load_game():
    if not os.path.exists(SAVE_FILE):
        print("\nNo save file found.")
        return None
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            lines = [line.rstrip("\n") for line in f if line.strip() != ""]
        if len(lines) < 2:
            raise ValueError("Save file has missing lines (expected 2).")

        stats = lines[0].split("|")
        potions = lines[1].split("|")
        if len(stats) != 8 or len(potions) != 3:
            raise ValueError("Save file fields are incomplete or malformed.")

        player = {
            "Name": stats[0],
            "HP": float(stats[1]),
            "maxHP": float(stats[2]),
            "ATK": int(stats[3]),
            "DEF": int(stats[4]),
            "SPD": int(stats[5]),
            "Gold": int(stats[6]),
            "Day": int(stats[7]),
            "Potion": {
                "Small": int(potions[0]),
                "Big": int(potions[1]),
                "Panacea": int(potions[2]),
            },
        }
        print("\nGame loaded successfully.")
        return player
    except Exception as e:
        print(f"Error loading game: {e}")
        return None

def verify_save():
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            non_empty = [ln for ln in f if ln.strip()]
        if len(non_empty) == 2:
            print("Verification complete: Save file is readable.\n")
            return True
        else:
            print("Warning: Save file format may be incorrect.\n")
            return False
    except Exception:
        print("Warning: Save file may be corrupted.\n")
        return False