Title: Reincarnated as a Devourer
Course: CMSC 12
Project: Terminal-based RPG
Developer: Charles Satoshi
Section: [Insert Section Here]
Date Started: 10/27/2025
Python Version: [Insert Version, e.g., Python 3.12.1]

Description:
Reincarnated as a Devourer is a terminal-based RPG where you awaken in another world after death, granted the forbidden power of Devour by a mysterious goddess. This power lets you absorb the strength of your defeated enemies. You have twenty days to train, explore, and grow strong enough to face the Demon King. As you gain power, you uncover a tragic secret that binds the goddess and the Demon King together. Your final battle will decide their fate — and yours.

Gameplay Overview:

Train to increase your stats.

Explore forests to battle monsters and earn gold.

Use the Devour skill to absorb stat bonuses from victories.

Visit the shop to buy weapons, armor, and potions.

Rest to recover HP and advance the day.

Save or load your progress anytime.

On Day 20, face the Demon King in the final battle.

Story Summary:
You died in your world and were reborn by a goddess who gave you the power of Devour. She tasks you with defeating the Demon King, a being of immense power. As days pass, you learn the truth — the goddess and the Demon King were once lovers, cursed by fate and time. You are her final creation, meant not to save the world but to set him free. After your victory, you awaken in a hospital, seeing a young couple who resemble them. You whisper, “Another world?”

File Structure:
main.py – Controls the start menu and main game flow.
game_functions.py – Contains training, resting, exploring, shop, and status logic.
battle.py – Handles turn-based combat and damage calculations.
save_load.py – Manages saving and loading progress.
story_events.py – Contains day-based story dialogues and scenes.
README.txt – Project documentation.

How to Run:

Open a terminal in the project folder.

Run this command:
python main.py

Follow on-screen instructions to play.

Libraries Used:

random (for stat and event randomization)

os (for clearing the terminal screen, optional)

Built-in Python file I/O functions for saving and loading.

Planned Additions:

Bonus dialogues after battles.

Optional ending based on player choices.

Additional story interactions during rest days.

Notes:
This project follows the CMSC 12 implementation rules:

No external libraries.

No classes (non-OOP).

Terminal-based interface only.

ASCII art and story flavor are optional but encouraged.