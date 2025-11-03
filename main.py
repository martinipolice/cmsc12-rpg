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
        print("[4] Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            start_game()
        elif choice == "2":
            player = save_load.load_game()
            if player:
                start_game(player)
        elif choice == "3":
            show_about()
        elif choice == "4":
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
        elif choice == "2":
            game_functions.rest(player)
        elif choice == "3":
            game_functions.explore(player)
        elif choice == "4":
            game_functions.shop(player)
        elif choice == "5":
            save_load.save_game(player)
        elif choice == "6":
            game_functions.show_stats(player)
        elif choice == "7":
            print("\nThank you for playing. Goodbye!\n")
            break
        else:
            print("\nInvalid input. Try again.\n")
    

        if player["Day"] > 20:
            print("\nYour 20 days are over. The final battle awaits...\n")
            game_functions.final_battle(player)
            break

            

def show_about():
    print("\nReincarnated as a Devourer is a terminal-based RPG.")
    print("You were reborn by a goddess with the Devour power.")
    print("Train, explore, and prepare to face the Demon King in 20 days.\n")
    input("(Press Enter to return to menu...)")


if __name__ == "__main__":
    main()
