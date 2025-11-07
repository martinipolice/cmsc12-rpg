# main.py
import game_functions
import save_load
import battle


def main():
    while True:
        print("=== REINCARNATED AS A DEVOURER ===")
        print("[1] Start Game")
        print("[2] Load Game")
        print("[3] About")
        print("[4] Help")
        print("[5] Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            start_game()
        elif choice == "2":
            player = save_load.load_game()
            if player:
                cont = input("Continue your journey? (Y/N): ").strip().lower()
                if cont == "y":
                    start_game(player)
                else:
                    print("Returning to menu...\n")
        elif choice == "3":
            show_about()
        elif choice == "4":
            show_help()
        elif choice == "5":
            print("\nGoodbye.\n")
            break
        else:
            print("\nInvalid input. Try again.\n")


def start_game(player=None):
    if not player:
        player = game_functions.create_player()

    while True:
        print(f"\n=== DAY {player['Day']} ===")
        print(f"What will you do today, {player['Name']}?")
        print("[1] Train")
        print("[2] Rest")
        print("[3] Explore")
        print("[4] Shop")
        print("[5] Save Game")
        print("[6] View Status")
        print("[7] End Game")

        choice = input("Choose an action: ")

        if choice == "1":
            game_functions.train(player)
            ask = input("Would you like to save your progress? (Y/N): ").strip().lower()
            if ask == "y":
                save_load.save_game(player)
        elif choice == "2":
            game_functions.rest(player)
            ask = input("Would you like to save your progress? (Y/N): ").strip().lower()
            if ask == "y":
                save_load.save_game(player)                
        elif choice == "3":
            game_functions.explore(player)
            ask = input("Would you like to save your progress? (Y/N): ").strip().lower()
            if ask == "y":
                save_load.save_game(player)
        elif choice == "4":
            game_functions.shop(player)
            ask = input("Would you like to save your progress? (Y/N): ").strip().lower()
            if ask == "y":
                save_load.save_game(player)
        elif choice == "5":
            save_load.save_game(player)
        elif choice == "6":
            game_functions.show_stats(player)
        elif choice == "7":
            confirm = input("Are you sure you want to quit? (Y/N): ").strip().lower()
            if confirm == "y":
                print("\nThank you for playing. Goodbye!\n")
                break
            else:
                print("\nContinuing your adventure...")
        else:
            print("\nInvalid input. Try again.\n")
    

        if player["Day"] > 20:
            print("\nYour 20 days are over. The final battle awaits...\n")
            game_functions.final_battle(player)
            print("\nThank you for playing 'Reincarnated as a Devourer'.")
            print("Developed by Charles Gian L. Santos.\n")
            break

            

def show_about():
    print("\nReincarnated as a Devourer is a terminal-based RPG.")
    print("You were reborn by a goddess with the Devour power.")
    print("Train, explore, and prepare to face the Demon King in 20 days.\n")
    input("(Press Enter to return to menu...)")

def show_help():
    print("\n=== HELP / TUTORIAL ===")
    print("1. Train to increase your stats and grow stronger.")
    print("2. Rest to fully restore your HP.")
    print("3. Explore to fight monsters and earn Gold.")
    print("4. Visit the Shop to buy potions and gear.")
    print("5. Always save your progress using the Save option.")
    print("6. Survive for 20 days, then face the Demon King.")
    input("\n(Press Enter to return to the menu...)")

if __name__ == "__main__":
    main()
