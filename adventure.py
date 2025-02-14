"""Enhanced text-based adventure game with inventory and dungeon exploration."""
import random

def display_player_status(player_health):
    """Prints player's current health."""
    print(f"Your current health: {player_health}")

def acquire_item(inventory, item):
    """Adds an item to the inventory and prints a message."""
    inventory.append(item)
    print(f"You acquired a {item}!")
    return inventory

def display_inventory(inventory):
    """Displays the player's inventory."""
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item}")

def enter_dungeon(player_health, inventory, dungeon_rooms):
    """Handles dungeon exploration including item acquisition and challenges."""
    for desc, item, challenge_type, outcome in dungeon_rooms:
        print(f"You enter: {desc}")
        if item:
            acquire_item(inventory, item)
        if challenge_type == "none":
            print("There doesn't seem to be a challenge in this room. You move on.")
        else:
            action = None  # Ensure action is always assigned
            if challenge_type == "trap":
                print("You see a potential trap!")
                action = input("Do you want to disarm or bypass it? ").lower()
            elif challenge_type == "puzzle":
                action = input("You encounter a puzzle! Solve or skip? ").lower()

            if action in ["solve", "disarm"]:
                success = random.choice([True, False])
                print(outcome[0] if success else outcome[1])
                player_health = max(player_health + outcome[2], 0)
                if player_health == 0:
                    print("You are barely alive!")
            else:
                print("You chose to avoid the challenge.")

        display_inventory(inventory)
    display_player_status(player_health)
    return player_health, inventory

def main():
    """Main function to initialize game variables and start the adventure."""
    player_health = 100
    inventory = []
    dungeon_rooms = [
        ("A dusty library", "key", "puzzle", \
         ("Puzzle solved!", "Puzzle failed!", -5)),
        ("A creaky floor passage", None, "trap",\
         ("Trap disarmed!", "You triggered the trap!", -10)),
        ("A shimmering pool hall", "potion", "none", None),
        ("A locked chest room", "treasure", "puzzle", \
         ("Chest opened!", "Chest locked!", -5))
    ]
    player_health, inventory = enter_dungeon(player_health, inventory, dungeon_rooms)
    try:
        dungeon_rooms[0] = ("Modified room", "new item", "trap", ("Success!", "Failure!", -5))
    except TypeError:
        print("Tuples are immutable! Cannot modify room data.")

if __name__ == "__main__":
    main()
