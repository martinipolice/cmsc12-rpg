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
            print("\nLoad feature coming soon.\n")
        elif choice == "3":
            show_about()
        elif choice == "4":
            print("\nGoodbye.\n")
            break
        else:
            print("\nInvalid input. Try again.\n")


def start_game():
    player = game_functions.create_player()

    while True:
        print(f"\n=== DAY {player['Day']} ===")
        print(f"What will you do today, {player['Name']}?")
        print("[1] Train")
        print("[2] Explore")
        print("[3] Rest")
        print("[4] View Status")
        print("[5] End Game")

        choice = input("Choose an action: ")

        if choice == "1":
            print("\nYou begin training. (Feature coming soon)\n")
            player["Day"] += 1
        elif choice == "2":
            print("\nYou explore the forest. (Feature coming soon)\n")
            player["Day"] += 1
        elif choice == "3":
            print("\nYou rest and recover your strength.\n")
            player["HP"] = player["maxHP"]
            player["Day"] += 1
        elif choice == "4":
            game_functions.show_stats(player)
        elif choice == "5":
            print("\nYou decided to end your journey early.\n")
            break
        else:
            print("\nInvalid input. Try again.\n")
        
        print(f"Day {player['Day']} has ended. You feel time slipping away...")
    

        if player["Day"] > 20:
            print("\nYour 20 days are over. The final battle awaits...\n")
            break



def show_about():
    print("\nReincarnated as a Devourer is a terminal-based RPG.")
    print("You were reborn by a goddess with the Devour power.")
    print("Train, explore, and prepare to face the Demon King in 20 days.\n")
    input("(Press Enter to return to menu...)")


if __name__ == "__main__":
    main()
