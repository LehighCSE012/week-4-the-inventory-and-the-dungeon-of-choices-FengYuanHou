"""This is an enhanced text-based adventure game with inventory and dungeon exploration."""
import random

def display_player_status(player_health):
    print(f"Your current health: {player_health}")

def acquire_item(inventory, item):
    inventory.append(item)
    print(f"You acquired a {item}!")

def display_inventory(inventory):
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item}")

def enter_dungeon(player_health, inventory, dungeon_rooms):
    for room in dungeon_rooms:
        description, item, challenge_type, outcome = room
        print(f"You enter: {description}")
        if item:
            acquire_item(inventory, item)
        if challenge_type == "none":
            print("There doesn't seem to be a challenge in this room. You move on.")
        else:
            action = input(f"You encounter a {challenge_type}! Do you want to tackle it? (yes/no): ").lower()
            if action == "yes":
                success = random.choice([True, False])
                if success:
                    print(outcome[0])
                    player_health = max(player_health + outcome[2], 0)
                else:
                    print(outcome[1])
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
        ("A dusty old library", "key", "puzzle", ("You solved the puzzle!", "The puzzle remains unsolved.", -5)),
        ("A narrow passage with a creaky floor", None, "trap", ("You skillfully avoid the trap!", "You triggered a trap!", -10)),
        ("A grand hall with a shimmering pool", "healing potion", "none", None),
        ("A small room with a locked chest", "treasure", "puzzle", ("You cracked the code!", "The chest remains stubbornly locked.", -5))
    ]
    player_health, inventory = enter_dungeon(player_health, inventory, dungeon_rooms)
    try:
        dungeon_rooms[0] = ("Modified room", "new item", "trap", ("Success!", "Failure!", -5))
    except TypeError as e:
        print("Tuples are immutable! Cannot modify room data.")

if __name__ == "__main__":
    main()
