# game_functions.py
import random

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


def train(player):
    print("\nChoose a training type:")
    print("[1] Stamina Training  (Increase maxHP)")
    print("[2] Strength Training (Increase ATK)")
    print("[3] Resilience Training (Increase DEF)")
    print("[4] Dexterity Training (Increase SPD)")
    print("[5] Guts Training (Increase all stats)")
    print("[6] Cancel")

    choice = input("Enter your choice: ")

    if choice == "1":
        old_hp = player["maxHP"]
        gain = random.randint(5, 20)
        player["maxHP"] += gain
        print(f"\nYou focused on endurance. maxHP increased from {old_hp} to {player['maxHP']} (+{gain})")

    elif choice == "2":
        old_atk = player["ATK"]
        gain = random.randint(5, 20)
        player["ATK"] += gain
        print(f"\nYou built your strength. ATK increased from {old_atk} to {player['ATK']} (+{gain})")

    elif choice == "3":
        old_def = player["DEF"]
        gain = random.randint(5, 20)
        player["DEF"] += gain
        print(f"\nYou hardened your defenses. DEF increased from {old_def} to {player['DEF']} (+{gain})")

    elif choice == "4":
        old_spd = player["SPD"]
        gain = random.randint(5, 20)
        player["SPD"] += gain
        print(f"\nYou refined your agility. SPD increased from {old_spd} to {player['SPD']} (+{gain})")

    elif choice == "5":
        print("\nYou trained your guts, pushing every limit!")
        old_hp = player["maxHP"]
        old_atk = player["ATK"]
        old_def = player["DEF"]
        old_spd = player["SPD"]

        hp_gain = random.randint(5, 15)
        atk_gain = random.randint(5, 15)
        def_gain = random.randint(5, 15)
        spd_gain = random.randint(5, 15)

        player["maxHP"] += hp_gain
        player["ATK"] += atk_gain
        player["DEF"] += def_gain
        player["SPD"] += spd_gain

        print(f"maxHP: {old_hp} → {player['maxHP']} (+{hp_gain})")
        print(f"ATK: {old_atk} → {player['ATK']} (+{atk_gain})")
        print(f"DEF: {old_def} → {player['DEF']} (+{def_gain})")
        print(f"SPD: {old_spd} → {player['SPD']} (+{spd_gain})")

    elif choice == "6":
        print("\nYou skipped training for the day.")
        return
    else:
        print("\nInvalid choice. Training canceled.")
        return

    player["Day"] += 1
    print(f"\nDay {player['Day']} has ended. You feel stronger than before.")


def rest(player):
    print("\nYou took a full day to rest.")
    print(f"HP restored from {player['HP']} to {player['maxHP']}.")
    player["HP"] = player["maxHP"]
    player["Day"] += 1
    print(f"Day {player['Day']} has ended. You feel refreshed.\n")


def explore(player):
    print("\nYou venture into the forest...")
    tis = player["maxHP"] + player["ATK"] + player["DEF"] + player["SPD"]

    # Determine spawn probabilities based on TIS
    if tis < 100:
        monsters = ["Slime", "Mega Slime", "King Slime"]
        weights = [85, 10, 5]
    elif tis < 150:
        monsters = ["Slime", "Mega Slime", "King Slime"]
        weights = [45, 45, 10]
    else:
        monsters = ["Slime", "Mega Slime", "King Slime"]
        weights = [35, 35, 30]

    # Choose monster based on weighted probability
    monster = random.choices(monsters, weights=weights, k=1)[0]

    # Define monster stats
    if monster == "Slime":
        m_stats = {"HP": 50, "ATK": 8, "DEF": 8, "SPD": 8, "Gold": 10}
    elif monster == "Mega Slime":
        m_stats = {"HP": 100, "ATK": 20, "DEF": 20, "SPD": 20, "Gold": 50}
    else:
        m_stats = {"HP": 200, "ATK": 50, "DEF": 50, "SPD": 50, "Gold": 500}

    # Display encounter
    print(f"\nA wild {monster} appeared!")
    print(f"Stats - HP: {m_stats['HP']}, ATK: {m_stats['ATK']}, DEF: {m_stats['DEF']}, SPD: {m_stats['SPD']}")

    # Placeholder for upcoming battle feature
    print("\nBattle feature coming soon...")

    # Assume victory for now
    print(f"\nYou defeated the {monster}!")
    old_gold = player["Gold"]
    player["Gold"] += m_stats["Gold"]
    print(f"Gold increased from {old_gold} to {player['Gold']} (+{m_stats['Gold']})")

    # Consume a day
    player["Day"] += 1
    print(f"\nDay {player['Day']} has ended. You return safely from the forest.\n")


def shop():
    pass

def save():
    pass

def status():
    pass
