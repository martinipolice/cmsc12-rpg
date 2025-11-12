# save_load.py

import os

SAVE_FILE = "game.save"

def save_game(player):
    """Save current player data into a file using pipe delimiter."""
    try:
        fileHandle = open(SAVE_FILE, "w")
        
        # Write basic stats on first line (no trailing pipe)
        fileHandle.write(f"{player['Name']}|{player['HP']}|{player['maxHP']}|")
        fileHandle.write(f"{player['ATK']}|{player['DEF']}|{player['SPD']}|")
        fileHandle.write(f"{player['Gold']}|{player['Day']}\n")
        
        # Write potion data on second line (no trailing pipe)
        fileHandle.write(f"{player['Potion']['Small']}|")
        fileHandle.write(f"{player['Potion']['Big']}|")
        fileHandle.write(f"{player['Potion']['Panacea']}")
        
        fileHandle.close()
        print("\nProgress saved successfully.")
        verify_save()
    except Exception as e:
        print(f"Error saving game: {e}")


def load_game():
    """Load player data from a save file using pipe delimiter."""
    if not os.path.exists(SAVE_FILE):
        print("\nNo save file found.")
        return None

    try:
        fileHandle = open(SAVE_FILE, "r")
        
        lines = []
        for line in fileHandle:
            lines.append(line[:-1])  # Remove newline character
        
        fileHandle.close()
        
        # Parse first line (basic stats) and filter empty strings
        stats = [s for s in lines[0].split("|") if s]
        
        # Parse second line (potions) and filter empty strings
        potions = [p for p in lines[1].split("|") if p]
        
        # Reconstruct player dictionary - FIXED with proper closing braces
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
                "Panacea": int(potions[2])
            }
        }
        
        print("\nGame loaded successfully.")
        return player
        
    except Exception as e:
        print(f"Error loading game: {e}")
        return None

    
def verify_save():
    """Check if the saved game can be loaded properly."""
    try:
        fileHandle = open(SAVE_FILE, "r")
        
        line_count = 0
        for line in fileHandle:
            if line.strip():  # Only count non-empty lines
                line_count += 1
        
        fileHandle.close()
        
        if line_count == 2:
            print("Verification complete: Save file is readable.\n")
            return True
        else:
            print("Warning: Save file format may be incorrect.\n")
            return False
            
    except Exception:
        print("Warning: Save file may be corrupted.\n")
        return False