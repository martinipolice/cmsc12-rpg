# game_functions.py
import random
import battle
import save_load
import time
from text_utils import slow_print

def create_player():
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
    
    slow_print(f"\nWelcome, {name}. You awaken in a strange new world.")
    slow_print("The goddess whispers: 'Survive, grow, and face your fate.'\n")
    return player


def show_stats(player):
    """Display the player's current stats."""
    print("\n" + "="*40)
    print(" "*14 + "STATUS")
    print("="*40)
    print(f"  Name: {player['Name']}")
    print(f"  HP: {player['HP']:.1f}/{player['maxHP']:.1f}")
    print(f"  ATK: {player['ATK']}  |  DEF: {player['DEF']}  |  SPD: {player['SPD']}")
    print(f"  Gold: {player['Gold']}G")
    print(f"  Day: {player['Day']}")
    print("\n  Potions:")
    for potion_type, count in player['Potion'].items():
        print(f"    - {potion_type}: {count}")
    print("="*40 + "\n")


def train(player):
    print("\nChoose a training type:")
    print("[1] Stamina Training  (Increase maxHP)")
    print("[2] Strength Training (Increase ATK)")
    print("[3] Resilience Training (Increase DEF)")
    print("[4] Dexterity Training (Increase SPD)")
    print("[5] Guts Training (Increase ATK, DEF, SPD)")
    print("[6] Cancel")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        old_hp = player["maxHP"]
        gain = random.randint(5, 20)
        player["maxHP"] += gain
        slow_print(f"\nYou focused on endurance. maxHP increased from {old_hp} to {player['maxHP']} (+{gain})")

    elif choice == "2":
        old_atk = player["ATK"]
        gain = random.randint(5, 20)
        player["ATK"] += gain
        slow_print(f"\nYou built your strength. ATK increased from {old_atk} to {player['ATK']} (+{gain})")

    elif choice == "3":
        old_def = player["DEF"]
        gain = random.randint(5, 20)
        player["DEF"] += gain
        slow_print(f"\nYou hardened your defenses. DEF increased from {old_def} to {player['DEF']} (+{gain})")

    elif choice == "4":
        old_spd = player["SPD"]
        gain = random.randint(5, 20)
        player["SPD"] += gain
        slow_print(f"\nYou refined your agility. SPD increased from {old_spd} to {player['SPD']} (+{gain})")

    elif choice == "5":
        # FIXED: Guts training only increases ATK/DEF/SPD per spec (no maxHP)
        slow_print("\nYou trained your guts, pushing every limit!")
        old_atk = player["ATK"]
        old_def = player["DEF"]
        old_spd = player["SPD"]

        atk_gain = random.randint(5, 15)
        def_gain = random.randint(5, 15)
        spd_gain = random.randint(5, 15)

        player["ATK"] += atk_gain
        player["DEF"] += def_gain
        player["SPD"] += spd_gain

        print(f"ATK: {old_atk} -> {player['ATK']} (+{atk_gain})")
        print(f"DEF: {old_def} -> {player['DEF']} (+{def_gain})")
        print(f"SPD: {old_spd} -> {player['SPD']} (+{spd_gain})")

    elif choice == "6":
        slow_print("\nYou skipped training for the day.")
        return
    else:
        print("\nInvalid choice. Training canceled.")
        return

    
    slow_print(f"\nDay {player['Day']} has ended. You feel stronger than before.")
    player["Day"] += 1
    check_lore_event(player)


def rest(player):
    slow_print("\nYou took a full day to rest.")
    slow_print(f"HP restored from {player['HP']} to {player['maxHP']}.")
    player["HP"] = player["maxHP"]
    player["Day"] += 1
    slow_print(f"Day {player['Day']} has ended. You feel refreshed.\n")

    check_lore_event(player)


def explore(player):
    slow_print("\nYou venture into the forest...")
    tis = player["maxHP"] + player["ATK"] + player["DEF"] + player["SPD"]

    # Determine spawn probabilities based on TIS
    if tis < 100:
        monsters = ["Dreadling", "Vexclaw", "Plaguewing"]
        weights = [85, 10, 5]
        print(f"(Your Total Stats: {tis} - Weak monsters ahead)")
    elif tis < 150:
        monsters = ["Dreadling", "Vexclaw", "Plaguewing"]
        weights = [45, 45, 10]
        print(f"(Your Total Stats: {tis} - Moderate challenge)")
    else:
        monsters = ["Dreadling", "Vexclaw", "Plaguewing"]
        weights = [35, 35, 30]
        print(f"(Your Total Stats: {tis} - Dangerous territory!)")

    # Choose monster based on weighted probability
    monster = random.choices(monsters, weights=weights, k=1)[0]

    # Define monster stats
    if monster == "Dreadling":
        m_stats = {"HP": 50, "ATK": 8, "DEF": 8, "SPD": 8, "Gold": 10}
    elif monster == "Vexclaw":
        m_stats = {"HP": 100, "ATK": 20, "DEF": 20, "SPD": 20, "Gold": 50}
    else:
        m_stats = {"HP": 200, "ATK": 50, "DEF": 50, "SPD": 50, "Gold": 500}

    slow_print(f"\nYou encountered a {monster}!")

    # Start battle
    result = battle.start_battle(player, monster, m_stats)

    if result == "win":
        slow_print(f"\nYou return victorious from the forest.")
    elif result == "lose":
        slow_print("\nYou wake up later... barely alive. The goddess's voice echoes faintly.")
        player["HP"] = player["maxHP"] / 2  # FIXED: Use float division
    elif result == "run":
        slow_print(f"\nYou escaped and returned safely to your camp.")

    # FIXED: Always consume a day after exploring
    player["Day"] += 1
    print(f"\nDay {player['Day']} has ended. You return safely from the forest.\n")
    check_lore_event(player)


def shop(player):
    print("\n" + "="*40)
    print(" "*16 + "SHOP")
    print("="*40)
    print("Welcome to the merchant's stall!")
    print(f"Your Gold: {player['Gold']}G\n")
    print("--- WEAPONS ---")
    print("[1] Dull Blade [+10 ATK] - 30G")
    print("[2] Standard Greatsword [+25 ATK] - 60G")
    print("[3] Mithril Warblade [+50 ATK] - 100G")
    print("\n--- ARMOR ---")
    print("[4] Wooden Guard [+10 DEF] - 30G")
    print("[5] Steel Shield [+25 DEF] - 60G")
    print("[6] Hero's Guard [+50 DEF] - 100G")
    print("\n--- FOOTWEAR ---")
    print("[7] Leather Treads [+10 SPD] - 30G")
    print("[8] Padded Footguards [+25 SPD] - 60G")
    print("[9] Hermes' Boots [+50 SPD] - 100G")
    print("\n--- POTIONS ---")
    print("[10] Common Potion [+30 HP] - 15G")
    print("[11] High Potion [+100 HP] - 30G")
    print("[12] Flask of Rejuvenation [Full Heal] - 50G")
    print("\n[13] Exit Shop")
    print("="*40)

    choice = input("\nChoose an item to buy: ").strip()

    if choice == "13":
        print("You left the shop.")
        return

    items = {
        "1": ("ATK", 10, 30, "Dull Blade"),
        "2": ("ATK", 25, 60, "Standard Greatsword"),
        "3": ("ATK", 50, 100, "Mithril Warblade"),
        "4": ("DEF", 10, 30, "Wooden Guard"),
        "5": ("DEF", 25, 60, "Steel Shield"),
        "6": ("DEF", 50, 100, "Hero's Guard"),
        "7": ("SPD", 10, 30, "Leather Treads"),
        "8": ("SPD", 25, 60, "Padded Footguards"),
        "9": ("SPD", 50, 100, "Hermes' Boots"),
        "10": ("Potion", "Small", 15, "Common Potion"),
        "11": ("Potion", "Big", 30, "High Potion"),
        "12": ("Potion", "Panacea", 50, "Flask of Rejuvenation")
    }

    if choice in items:
        item_data = items[choice]
        stat = item_data[0]
        value = item_data[1]
        cost = item_data[2]
        item_name = item_data[3]
        
        if player["Gold"] < cost:
            slow_print(f"\nNot enough gold. You need {cost}G but only have {player['Gold']}G.")
            return

        player["Gold"] -= cost

        if stat == "Potion":
            player["Potion"][value] += 1
            slow_print(f"\nYou bought a {item_name} for {cost}G!")
            print(f"You now have {player['Potion'][value]} {value} Potion(s).")
            print(f"Remaining Gold: {player['Gold']}G")  # FIXED: Added
        else:
            old = player[stat]
            player[stat] += value
            slow_print(f"\nYou bought {item_name} for {cost}G!")
            print(f"{stat} increased: {old} -> {player[stat]} (+{value})")
            print(f"Remaining Gold: {player['Gold']}G")
    else:
        print("\nInvalid choice.")


def final_battle(player):
    print("\n" + "="*50)
    print("         THE FINAL BATTLE")
    print("="*50)
    slow_print("\nThe sky darkens... The Demon King descends before you!")
    

    # Demon King stats (base values)
    m_stats = {
        "HP": 200,
        "ATK": 75,
        "DEF": 75,
        "SPD": 75,
        "Gold": 0
    }

    slow_print("\nA blinding light fills the sky. The final battle begins!\n")

    monster_hp = m_stats["HP"]
    player_hp = player["HP"]
    turn_count = 1
    charge_next = False

    player_first = player["SPD"] >= m_stats["SPD"]

    while True:
        print(f"\n{'='*50}")
        print(f"--- Turn {turn_count} ---")
        print(f"Your HP: {player_hp}/{player['maxHP']}")
        print(f"Demon King HP: {monster_hp}/{m_stats['HP']}")
        print(f"{'='*50}")

        # Check if Demon King should charge (on turns 5, 10, 15, etc.)
        if turn_count % 5 == 0:
            print("\n*** CRITICAL MOMENT ***")
            slow_print("The Demon King begins to charge up immense power!")
            slow_print("Dark energy swirls around him...")
            slow_print("He's preparing a devastating attack for next turn!")
            charge_next = True
            turn_count += 1
            continue  # Skip to next turn

        if player_first:
            result = player_turn_boss(player, "Demon King", m_stats, player_hp, monster_hp)
            monster_hp = result["monster_hp"]
            player_hp = result["player_hp"]

            if result["fled"]:
                slow_print("\nYou tried to flee, but the goddess blocks your path.")
                slow_print("'You cannot run from fate,' her voice echoes.")
                turn_count += 1
                continue

            if monster_hp <= 0:
                victory_sequence(player)
                break

            # Restore defense after player's defend action
            if result.get("defending", False):
                player["DEF"] = result["original_def"]
                slow_print(f"Your defense returns to normal: {player['DEF']}")

            # Demon King's turn
            atk_boost = 2 if charge_next else 1
            damage = max(0, (m_stats["ATK"] * atk_boost) - player["DEF"])
            
            if charge_next:
                print("\n*** CHARGED ATTACK UNLEASHED! ***")
                slow_print("The Demon King releases his stored power!")
                charge_next = False
            
            player_hp -= damage
            player_hp = max(0, player_hp)
            slow_print(f"The Demon King dealt {damage} damage!")

            if player_hp <= 0:
                defeat_sequence()
                break

        else:
            # Demon King attacks first
            atk_boost = 2 if charge_next else 1
            damage = max(0, (m_stats["ATK"] * atk_boost) - player["DEF"])
            
            if charge_next:
                print("\n*** CHARGED ATTACK UNLEASHED! ***")
                slow_print("The Demon King releases his stored power!")
                charge_next = False
            
            player_hp -= damage
            player_hp = max(0, player_hp)
            slow_print(f"The Demon King dealt {damage} damage!")

            if player_hp <= 0:
                defeat_sequence()
                break

            result = player_turn_boss(player, "Demon King", m_stats, player_hp, monster_hp)
            monster_hp = result["monster_hp"]
            player_hp = result["player_hp"]

            if result["fled"]:
                slow_print("\nYou tried to flee, but the goddess blocks your path.")
                slow_print("'You cannot run from fate,' her voice echoes.")
                turn_count += 1
                continue

            # Restore defense after player's defend action
            if result.get("defending", False):
                player["DEF"] = result["original_def"]
                slow_print(f"Your defense returns to normal: {player['DEF']}")

            if monster_hp <= 0:
                victory_sequence(player)
                break

        turn_count += 1

    print("\n" + "="*50)
    print("=== GAME OVER ===")
    print("="*50)


def player_turn_boss(player, monster_name, m_stats, player_hp, monster_hp):
    """Handles player's turn in boss battle."""
    print("\nChoose your action:")
    print("[1] Attack")
    print("[2] Defend")
    print("[3] Item")
    print("[4] Flee (Blocked by fate)")

    choice = input("Enter your choice: ").strip()

    fled = False
    defending = False
    original_def = player["DEF"]

    if choice == "1":
        damage = max(0, player["ATK"] - m_stats["DEF"])
        monster_hp -= damage
        slow_print(f"\nYou attacked the {monster_name} for {damage} damage!")

    elif choice == "2":
        defending = True
        player["DEF"] += player["ATK"]
        slow_print(f"\nYou brace yourself!")
        slow_print(f"DEF: {original_def} -> {player['DEF']}")

    elif choice == "3":
        potions = player["Potion"]
        print("\nAvailable Potions:")
        for p, count in potions.items():
            print(f"  {p}: {count}")

        select = input("Choose a potion (Small/Big/Panacea): ").strip().capitalize()

        if select == "Small" and potions["Small"] > 0:
            heal = 30
            player_hp = min(player["maxHP"], player_hp + heal)
            potions["Small"] -= 1
            slow_print(f"Used Small Potion! Restored {heal} HP!")
            slow_print(f"Current HP: {player_hp}/{player['maxHP']}")

        elif select == "Big" and potions["Big"] > 0:
            heal = 100
            player_hp = min(player["maxHP"], player_hp + heal)
            potions["Big"] -= 1
            slow_print(f"Used Big Potion! Restored {heal} HP!")
            slow_print(f"Current HP: {player_hp}/{player['maxHP']}")

        elif select == "Panacea" and potions["Panacea"] > 0:
            player_hp = player["maxHP"]
            potions["Panacea"] -= 1
            slow_print("Used Panacea! Fully restored HP!")
            slow_print(f"Current HP: {player_hp}/{player['maxHP']}")

        else:
            slow_print("Invalid choice or no potions! Turn wasted!")

    elif choice == "4":
        fled = True  # Will be handled in main battle loop
    else:
        slow_print("\nInvalid input! You hesitate!")

    return {
        "monster_hp": monster_hp, 
        "player_hp": player_hp, 
        "fled": fled,
        "defending": defending,
        "original_def": original_def
    }


def victory_sequence(player):
    """Victory cutscene."""
    print("\n" + "="*50)
    print("\n         VICTORY")
    print("\n" + "="*50)
    
    def say(text, delay=1.5):
        print(text)
        time.sleep(delay)
    
    slow_print("\nThe Demon King falls to his knees...")
    time.sleep(0.8)
    slow_print("A faint smile crosses his face.")
    time.sleep(0.8)
    slow_print("\nDemon King: 'Finally... Tell her... I waited.'")
    time.sleep(0.8)
    slow_print("\nLight floods the ruined temple.")
    time.sleep(0.8)
    slow_print("The goddess appears, tears streaming down her face.")
    time.sleep(0.8)
    slow_print("\nGoddess: 'Thank you, brave soul.'")
    time.sleep(0.8)
    slow_print("Goddess: 'His soul can rest now... and so can mine.'")
    time.sleep(0.8)
    slow_print("\nThey reach for each other as they begin to fade.")
    time.sleep(0.8)
    slow_print("Their forms dissolve into light, intertwining as they vanish.")
    time.sleep(0.8)
    slow_print("\nSilence follows.")
    time.sleep(0.8)
    slow_print("The world feels... empty.")

    player["Day"] = 21
    check_lore_event(player)


def defeat_sequence():
    """Defeat cutscene."""
    print("\n" + "="*50)
    print("\n         DEFEAT")
    print("\n" + "="*50)
    
    def say(text, delay=1.5):
        print(text)
        time.sleep(delay)
    
    slow_print("\nYou have fallen in battle...")
    time.sleep(0.8)
    slow_print("The Demon King stands over you, unmoved.")
    time.sleep(0.8)
    slow_print("\nDemon King: 'Not strong enough. She chose poorly.'")
    time.sleep(0.8)
    slow_print("\nThe world plunges into darkness once more.")
    time.sleep(0.8)
    slow_print("The goddess weeps in silence.")
    time.sleep(0.8)
    slow_print("\nThe cycle remains unbroken.")


def check_lore_event(player):
    day = player["Day"]

    if day == 1:
        slow_print("\nYou wake up in a forest. The air feels heavy and still.", delay=0.04)
        time.sleep(0.8)
        slow_print("A faint voice echoes: 'This world is your new beginning.'", delay=0.04)

    elif day == 5:
        slow_print("\nYou dream of the goddess watching from afar.", delay=0.04)
        time.sleep(0.8)
        slow_print("Goddess: 'Do not fear this world. It was made for you.'", delay=0.04)

    elif day == 10:
        slow_print("\nA vision fills your mind.", delay=0.04)
        time.sleep(0.8)
        slow_print("You see the goddess beside a shadow under a red sky.", delay=0.04)
        time.sleep(0.8)
        slow_print("Her voice trembles: 'Forgive me.'", delay=0.04)

    elif day == 11:
        slow_print("\nThe dreams feel too real to ignore.", delay=0.04)
        time.sleep(0.8)
        slow_print("You begin to wonder who the man beside her was.", delay=0.04)

    elif day == 15:
        slow_print("\nYou find ancient ruins deep within the forest.", delay=0.04)
        time.sleep(0.8)
        slow_print("Carvings show a goddess and a dark figure side by side.", delay=0.04)
        time.sleep(0.8)
        slow_print("Ghostly Voice: 'They once loved each other. Love turned to ruin.'", delay=0.04)
        time.sleep(0.8)
        slow_print("Goddess: 'Do not question fate. Finish what was started.'", delay=0.04)

    elif day == 16:
        slow_print("\nThe goddess no longer answers.", delay=0.04)
        time.sleep(0.8)
        slow_print("The monsters whisper your name as you fight.", delay=0.04)

    elif day == 19:
        slow_print("\nYou dream once more. The goddess appears, fading fast.", delay=0.04)
        time.sleep(0.8)
        slow_print("Goddess: 'He waits for me still... End it, please.'", delay=0.04)

    elif day == 20:
        slow_print("\nYou reach a ruined temple. Darkness thickens around you.", delay=0.04)
        time.sleep(0.8)
        slow_print("A tall figure steps forward.", delay=0.04)
        time.sleep(0.8)
        slow_print("Demon King: 'You carry her scent... and her sorrow.'", delay=0.04)
        time.sleep(0.8)
        slow_print("You: 'She sent me to end you.'", delay=0.04)
        time.sleep(0.8)
        slow_print("Demon King: 'Then she still cannot let go.'", delay=0.04)

    elif day == 21:
        print("\n" + "="*50)
        time.sleep(1.5)
        slow_print("The world dissolves into white...", delay=0.05)
        time.sleep(2)
        slow_print("", delay=0.05)
        time.sleep(1)
        slow_print("*Beep... Beep...*", delay=0.05)
        time.sleep(1.5)
        slow_print("", delay=0.05)
        time.sleep(1)
        slow_print("You open your eyes in a hospital room.", delay=0.05)
        time.sleep(2)
        slow_print("Sterile walls. The smell of antiseptic.", delay=0.05)
        time.sleep(2)
        slow_print("", delay=0.05)
        time.sleep(1)
        slow_print("Through the window, a young couple walks by.", delay=0.05)
        time.sleep(2.5)
        slow_print("Their faces... they resemble the goddess and the Demon King.", delay=0.05)
        time.sleep(2.5)
        slow_print("", delay=0.05)
        time.sleep(1)
        slow_print("You whisper: 'Another world?'", delay=0.05)
        time.sleep(2)
        slow_print("", delay=0.05)
        time.sleep(1)
        slow_print("The door opens. A nurse smiles at you.", delay=0.05)
        time.sleep(2)
        slow_print("'Welcome back. You've been asleep for 20 days.'", delay=0.05)
        time.sleep(2.5)
        slow_print("", delay=0.05)
        time.sleep(2)
        print("="*50)
        time.sleep(1)