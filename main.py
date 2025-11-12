# main.py
import game_functions
import save_load
import battle


def main():
    while True:
        print("\n" + "="*50)
        print("           REINCARNATED AS A DEVOURER")
        print("="*50)
        print("[1] Start Game")
        print("[2] Load Game")
        print("[3] About")
        print("[4] Help")
        print("[5] Exit")
        print("="*50)

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            start_game()
        elif choice == "2":
            player = save_load.load_game()
            if player:
                print(f"\nWelcome back, {player['Name']}!")
                print(f"Current Day: {player['Day']}")
                print(f"HP: {player['HP']}/{player['maxHP']}")
                cont = input("\nContinue your journey? (Y/N): ").strip().lower()
                if cont == "y":
                    start_game(player)
                else:
                    print("Returning to menu...\n")
        elif choice == "3":
            show_about()
        elif choice == "4":
            show_help()
        elif choice == "5":
            print("\nThank you for playing!")
            print("May your next journey be legendary.\n")
            break
        else:
            print("\nInvalid input. Please choose 1-5.\n")


def start_game(player=None):
    if not player:
        player = game_functions.create_player()

    while True:
        print("\n" + "="*50)
        print(f"           DAY {player['Day']}")
        print("="*50)
        print(f"What will you do today, {player['Name']}?")
        print("\n[1] Train      - Improve your stats")
        print("[2] Rest       - Restore HP to full")
        print("[3] Explore    - Fight monsters for gold")
        print("[4] Shop       - Buy equipment and potions")
        print("[5] Save Game  - Save your progress")
        print("[6] Status     - View your stats")
        print("[7] End Game   - Quit to main menu")
        print("="*50)

        choice = input("\nChoose an action: ").strip()

        if choice == "1":
            game_functions.train(player)
            ask = input("\nSave your progress? (Y/N): ").strip().lower()
            if ask == "y":
                save_load.save_game(player)
                
        elif choice == "2":
            game_functions.rest(player)
            ask = input("\nSave your progress? (Y/N): ").strip().lower()
            if ask == "y":
                save_load.save_game(player)
                
        elif choice == "3":
            game_functions.explore(player)
            ask = input("\nSave your progress? (Y/N): ").strip().lower()
            if ask == "y":
                save_load.save_game(player)
                
        elif choice == "4":
            game_functions.shop(player)
            ask = input("\nSave your progress? (Y/N): ").strip().lower()
            if ask == "y":
                save_load.save_game(player)
                
        elif choice == "5":
            save_load.save_game(player)
            
        elif choice == "6":
            game_functions.show_stats(player)
            
        elif choice == "7":
            confirm = input("\nAre you sure you want to quit? (Y/N): ").strip().lower()
            if confirm == "y":
                print("\nThank you for playing. Your journey pauses here...\n")
                break
            else:
                print("\nContinuing your adventure...")
        else:
            print("\nInvalid input. Please choose 1-7.\n")
    
        # FIXED: Check if Day 20 has arrived - trigger final boss
        if player["Day"] == 20:
            print("\n" + "="*50)
            print("\n YOUR 20 DAYS ARE OVER")
            print("     The final battle awaits...")
            print("\n" + "="*50 + "\n")
            input("Press Enter to face your fate...")
            
            game_functions.final_battle(player)
            
            print("\n" + "="*50)
            print("Thank you for playing")
            print("'Reincarnated as a Devourer'")
            print("\nDeveloped by Charles Gian L. Santos")
            print("="*50 + "\n")
            break


def show_about():
    print("\n" + "="*50)
    print("              ABOUT")
    print("="*50)
    print("\nGame Title: REINCARNATED AS A DEVOURER")
    print("\nYou were reborn by a goddess into a strange world.")
    print("Gifted with the power to Devour, you must grow")
    print("stronger and face your destiny.")
    print("\nTrain. Explore. Survive.")
    print("In 20 days, you will face the Demon King.")
    print("\nBut the truth behind your mission...")
    print("...may not be what it seems.")
    print("\n" + "-"*50)
    print("Developer: Charles Gian L. Santos")
    print("Lab Section: [Your Section Here]")  # FIXED: Added
    print("Student Number: [Your Number Here]")  # FIXED: Added
    print("CMSC 12 Project - Terminal-based RPG")
    print("="*50)
    input("\n(Press Enter to return to menu...)")


def show_help():
    print("\n" + "="*50)
    print("          HELP / TUTORIAL")
    print("="*50)
    print("\nOBJECTIVE:")
    print("  Survive for 20 days and defeat the Demon King")
    print("\nDAILY ACTIVITIES:")
    print("  - Train    : Increase your stats (consumes 1 day)")
    print("  - Rest     : Fully restore your HP (consumes 1 day)")
    print("  - Explore  : Fight monsters, earn Gold (consumes 1 day)")
    print("  - Shop     : Buy weapons, armor, potions (no time cost)")
    print("  - Save     : Save your progress (no time cost)")
    print("  - Status   : View your stats (no time cost)")
    print("\nCOMBAT TIPS:")
    print("  - Higher SPD = You attack first")
    print("  - Defend adds your ATK to DEF for one turn")
    print("  - Potions can save your life in tough battles")
    print("  - You can flee, but it's only 50% successful")
    print("\nSTRATEGY:")
    print("  - Balance training with exploring for gold")
    print("  - Buy equipment early to survive stronger monsters")
    print("  - Save often! You can lose progress if defeated")
    print("  - Pay attention to the story events...")
    print("\n" + "="*50)
    input("\n(Press Enter to return to menu...)")


if __name__ == "__main__":
    main()