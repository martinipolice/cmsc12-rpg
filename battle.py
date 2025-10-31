# battle.py
import random

def start_battle(player, monster_name, m_stats):
    print(f"\nA wild {monster_name} appeared!")
    print(f"Stats - HP: {m_stats['HP']}, ATK: {m_stats['ATK']}, DEF: {m_stats['DEF']}, SPD: {m_stats['SPD']}")
    print(f"\nA battle begins against {monster_name}!")
    print("Prepare yourself!\n")

    monster_hp = m_stats["HP"]
    player_hp = player["HP"]
    turn_count = 1

    # Determine SPD-based order
    player_first = player["SPD"] >= m_stats["SPD"]

    while True:
        print(f"\n--- Turn {turn_count} ---")
        print(f"Your HP: {player_hp}/{player['maxHP']}")
        print(f"{monster_name} HP: {monster_hp}")

        # Player moves first
        if player_first:
            result = player_turn(player, monster_name, m_stats, player_hp, monster_hp)

            # store old defense if defending
            if "temp_def" in result and player["DEF"] > result["temp_def"]:
                player["temp_def"] = result["temp_def"]

            # check win or flee
            if result["monster_hp"] <= 0:
                print(f"\nYou defeated the {monster_name}!")
                gold = m_stats["Gold"]
                player["Gold"] += gold
                print(f"You earned {gold} Gold.")
                player["HP"] = player_hp
                return "win"
            if result["fled"]:
                print(f"\nYou successfully fled from the {monster_name}.")
                player["HP"] = player_hp
                return "run"

            monster_hp = result["monster_hp"]
            player_hp = result["player_hp"]

            # enemy's turn
            player_hp = enemy_turn(player_hp, player, monster_name, m_stats)
            if player_hp <= 0:
                print("\nYou have fallen in battle...")
                player["HP"] = 0
                return "lose"

        # Enemy moves first
        else:
            player_hp = enemy_turn(player_hp, player, monster_name, m_stats)
            if player_hp <= 0:
                print("\nYou have fallen in battle...")
                player["HP"] = 0
                return "lose"

            result = player_turn(player, monster_name, m_stats, player_hp, monster_hp)

            if "temp_def" in result and player["DEF"] > result["temp_def"]:
                player["temp_def"] = result["temp_def"]

            if result["monster_hp"] <= 0:
                print(f"\nYou defeated the {monster_name}!")
                gold = m_stats["Gold"]
                player["Gold"] += gold
                print(f"You earned {gold} Gold.")
                player["HP"] = player_hp
                return "win"
            if result["fled"]:
                print(f"\nYou successfully fled from the {monster_name}.")
                player["HP"] = player_hp
                return "run"

            monster_hp = result["monster_hp"]
            player_hp = result["player_hp"]

        turn_count += 1


def player_turn(player, monster_name, m_stats, player_hp, monster_hp):
    """Handles player's turn actions."""
    print("\nChoose your action:")
    print("[1] Attack")
    print("[2] Defend")
    print("[3] Item")
    print("[4] Flee")

    choice = input("Enter your choice: ")

    fled = False
    temp_def = player["DEF"]

    if choice == "1":
        damage = max(0, player["ATK"] - m_stats["DEF"])
        monster_hp -= damage
        print(f"\nYou attacked the {monster_name} for {damage} damage!")

    elif choice == "2":
        player["DEF"] += player["ATK"]
        print(f"\nYou brace yourself for the attack! DEF temporarily increased to {player['DEF']}.")

    elif choice == "3":
        print("\nItem system coming soon.")
        # placeholder for potion use

    elif choice == "4":
        chance = random.randint(1, 100)
        if chance <= 50:
            fled = True
        else:
            print(f"\nYou tried to flee but failed! The {monster_name} blocks your path.")
            print("You lose your turn as the enemy prepares to strike.")
    else:
        print("\nInvalid input.")

    return {"monster_hp": monster_hp, "player_hp": player_hp, "fled": fled, "temp_def": temp_def}


def enemy_turn(player_hp, player, monster_name, m_stats):
    """Handles enemy's attack phase."""
    damage = max(0, m_stats["ATK"] - player["DEF"])
    player_hp -= damage
    print(f"The {monster_name} attacked and dealt {damage} damage!")

    # Revert defense after defend
    if "temp_def" in player:
        player["DEF"] = player["temp_def"]
        del player["temp_def"]

    return player_hp
