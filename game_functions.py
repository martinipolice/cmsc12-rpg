# game_functions.py


def create_player():
    """Create a new player using CMSC12 spec format."""
    name = input("Enter your name: ")

    player = {
        "Name": name,
        "HP": 20.0,
        "maxHP": 30.0,
        "ATK": 5,
        "DEF": 5,
        "SPD": 5,
        "Gold": 30,
        "Potion": {"Small": 0, "Big": 0, "Panacea": 0},
        "Day": 1
    }

    print(f"\nWelcome, {name}. You awaken in a strange new world.")
    print("The goddess whispers: 'Survive, grow, and face your fate.'\n")
    return player


def show_stats(player):
    """Display the player's current stats."""
    print("\n===== STATUS =====")
    print(f"Name: {player['Name']}")
    print(f"HP: {player['HP']}/{player['maxHP']}")
    print(f"ATK: {player['ATK']}")
    print(f"DEF: {player['DEF']}")
    print(f"SPD: {player['SPD']}")
    print(f"Gold: {player['Gold']}")
    print(f"Potions: {player['Potion']}")
    print(f"Day: {player['Day']}")
    print("==================\n")




def train():
    pass

def rest():
    pass

def explore():
    pass

def shop():
    pass

def save():
    pass

def status():
    pass
