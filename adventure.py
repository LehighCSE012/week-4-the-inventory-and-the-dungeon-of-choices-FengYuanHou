"""Enhanced text-based adventure game with inventory and dungeon exploration."""
import random

def display_player_status(player_health):
    print(f"Your current health: {player_health}")

def acquire_item(inventory, item):
    inventory.append(item)
    print(f"You found a {item} in the room.")
    return inventory

def display_inventory(inventory):
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item}")

def enter_dungeon(player_health, inventory, dungeon_rooms):
    for description, item, challenge_type, outcome in dungeon_rooms:
        print(f"You enter: {description}")
        if item:
            acquire_item(inventory, item)
        if challenge_type == "none":
            print("There doesn't seem to be a challenge in this room. You move on.")
        else:
            action = input(f"You encounter a {challenge_type}! Do you want to solve/disarm or skip/bypass it? ").lower()
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
    player_health = 100
    inventory = []
    dungeon_rooms = [
        ("A dusty old library", "key", "puzzle", ("Puzzle solved!", "Puzzle failed!", -5)),
        ("A narrow passage with a creaky floor", None, "trap", ("Trap disarmed!", "You triggered the trap!", -10)),
        ("A grand hall with a shimmering pool", "healing potion", "none", None),
        ("A small room with a locked chest", "treasure", "puzzle", ("Chest opened!", "Chest locked!", -5))
    ]
    player_health, inventory = enter_dungeon(player_health, inventory, dungeon_rooms)
    try:
        dungeon_rooms[0] = ("Modified room", "new item", "trap", ("Success!", "Failure!", -5))
    except TypeError:
        print("Tuples are immutable! Cannot modify room data.")

if __name__ == "__main__":
    main()
