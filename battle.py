# battle.py
import random
from text_utils import slow_print

def start_battle(player, monster_name, m_stats):
    slow_print(f"\nA battle begins against {monster_name}!")
    slow_print("Prepare yourself!\n")

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

            # check win or flee
            if result["monster_hp"] <= 0:
                slow_print(f"\nYou defeated the {monster_name}!")
                gold = m_stats["Gold"]
                old_gold = player["Gold"]
                player["Gold"] += gold
                slow_print(f"You earned {gold} Gold. ({old_gold} -> {player['Gold']})")
                player["HP"] = result["player_hp"]
                return "win"
            if result["fled"]:
                slow_print(f"\nYou successfully fled from the {monster_name}.")
                player["HP"] = result["player_hp"]
                return "run"

            monster_hp = result["monster_hp"]
            player_hp = result["player_hp"]

            # enemy's turn
            player_hp = enemy_turn(player_hp, player, monster_name, m_stats, result.get("defending", False), result.get("original_def", None))
            if player_hp <= 0:
                slow_print("\nYou have fallen in battle...")
                player["HP"] = 0
                return "lose"

        # Enemy moves first
        else:
            player_hp = enemy_turn(player_hp, player, monster_name, m_stats, False, None)
            if player_hp <= 0:
                slow_print("\nYou have fallen in battle...")
                player["HP"] = 0
                return "lose"

            result = player_turn(player, monster_name, m_stats, player_hp, monster_hp)

            if result["monster_hp"] <= 0:
                slow_print(f"\nYou defeated the {monster_name}!")
                gold = m_stats["Gold"]
                old_gold = player["Gold"]  # FIXED: Consistent old->new gold
                player["Gold"] += gold
                slow_print(f"You earned {gold} Gold. ({old_gold} -> {player['Gold']})")
                player["HP"] = result["player_hp"]
                return "win"
            if result["fled"]:
                slow_print(f"\nYou successfully fled from the {monster_name}.")
                player["HP"] = result["player_hp"]
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

    choice = input("Enter your choice: ").strip()

    fled = False
    defending = False
    original_def = player["DEF"]

    if choice == "1":
        damage = max(0, player["ATK"] - m_stats["DEF"])
        monster_hp -= damage
        slow_print(f"\nYou attacked the {monster_name} for {damage} damage!")
        print(f"(Your ATK {player['ATK']} vs Enemy DEF {m_stats['DEF']})")

    elif choice == "2":
        defending = True
        player["DEF"] += player["ATK"]
        slow_print(f"\nYou brace yourself for the attack!")
        print(f"DEF temporarily increased: {original_def} -> {player['DEF']}")

    elif choice == "3":
        potions = player["Potion"]
        print("\nAvailable Potions:")
        for p, count in potions.items():
            print(f"  {p}: {count}")
        print("[Cancel] - Type anything else to cancel")

        select = input("Choose a potion (Small/Big/Panacea): ").strip().capitalize()

        if select == "Small" and potions["Small"] > 0:
            heal = 30
            player_hp = min(player["maxHP"], player_hp + heal)
            potions["Small"] -= 1
            slow_print(f"You used a Small Potion and restored {heal} HP!")
            print(f"Current HP: {player_hp}/{player['maxHP']}")

        elif select == "Big" and potions["Big"] > 0:
            heal = 100
            player_hp = min(player["maxHP"], player_hp + heal)
            potions["Big"] -= 1
            slow_print(f"You used a Big Potion and restored {heal} HP!")
            print(f"Current HP: {player_hp}/{player['maxHP']}")

        elif select == "Panacea" and potions["Panacea"] > 0:
            player_hp = player["maxHP"]
            potions["Panacea"] -= 1
            slow_print("You used a Panacea and fully restored your HP!")
            print(f"Current HP: {player_hp}/{player['maxHP']}")

        else:
            print("Invalid choice or not enough potions. You wasted your turn!")

    elif choice == "4":
        chance = random.randint(1, 100)
        if chance <= 50:
            fled = True
        else:
            slow_print(f"\nYou tried to flee but failed! The {monster_name} blocks your path.")
            slow_print("You lose your turn as the enemy prepares to strike.")
    else:
        print("\nInvalid input. You hesitate and waste your turn!")

    # FIXED: Proper return statement with all closing braces
    return {
        "monster_hp": monster_hp, 
        "player_hp": player_hp, 
        "fled": fled,
        "defending": defending,
        "original_def": original_def
    }


def enemy_turn(player_hp, player, monster_name, m_stats, defending=False, original_def=None):
    """Handles enemy's attack phase."""
    damage = max(0, m_stats["ATK"] - player["DEF"])
    player_hp -= damage
    player_hp = max(0, player_hp)
    slow_print(f"The {monster_name} attacked and dealt {damage} damage!")
    print(f"(Enemy ATK {m_stats['ATK']} vs Your DEF {player['DEF']})")

    # Revert defense after defend
    if defending and original_def is not None:
        player["DEF"] = original_def
        print(f"Your defense returns to normal: {player['DEF']}")

    return player_hp