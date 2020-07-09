from room import Room
from player import Player
from item import Item

# items

item = {
    'bow': Item("Bow", "Always need a weapon of some sort"),
    'arrows': Item("Quiver of Arrows", "Can't shoot them with out the bow :/"),
    'sword': Item("Sword", "Slice and Dice the homies"),
    'boots': Item("Pair of Boots", "Walk over everything nicely"),
    'helmet': Item("Helmet", "Got to protect that head")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", item["boots"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", item["bow"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item["sword"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item["arrows"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",  item["helmet"]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

print("Welcome to Adventure Game!")
player_name = input("\nEnter your name: ")
new_player = Player(player_name, room['outside'])
print(f"\nWelcome, {new_player.name}.\n")
print(f"{new_player.current_room.description}.\033[0m \n")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:

    if new_player.current_room.items != None:
        print(f"You see a {new_player.current_room.items.name}.\n")
        pickup_item = input("Would you like to pick it up (y or n)?:").lower()
        if pickup_item == "y" or pickup_item == "yes":
            new_player.getItem(new_player.current_room.items)
            new_player.current_room.items = None
            print(f"\nYou now have:")
            for count, item in enumerate(new_player.items, 1):
                print(count, item)

    travel_direction = input(
        "\nWhat direction would you like to travel (n, s, w or e): ( (q) to exit the game) ").strip().lower()[0]

    if travel_direction == "s":
        if new_player.current_room.s_to == []:
            print("\n\033[1mYou checked, but South doesn't work.\033[0m")
        else:
            new_player.current_room = new_player.current_room.s_to
            print(
                f'\n\033[1mYou moved to {new_player.current_room.name}\033[0m \n')
            print(f"{new_player.current_room.description}.\033[0m \n")

    elif travel_direction == "w":
        if new_player.current_room.w_to == []:
            print("\n\033[1mYou checked, but West doesn't work.\033[0m")
        else:
            new_player.current_room = new_player.current_room.w_to
            print(
                f'\n\033[1mYou moved to {new_player.current_room.name}\033[0m \n')
            print(f"{new_player.current_room.description}.\033[0m \n")

    elif travel_direction == "e":
        if new_player.current_room.e_to == []:
            print("\n\033[1mYou checked, but East doesn't work.\033[0m")
        else:
            new_player.current_room = new_player.current_room.e_to
            print(
                f'\n\033[1mYou moved to {new_player.current_room.name}\033[0m \n')
            print(f"{new_player.current_room.description}.\033[0m \n")

    elif travel_direction == "n":
        if new_player.current_room.n_to == []:
            print("\n\033[1mYou checked, but North doesn't work.\033[0m")
        else:
            new_player.current_room = new_player.current_room.n_to
            print(
                f'\n\033[1mYou moved to {new_player.current_room.name}\033[0m \n')
            print(f"{new_player.current_room.description}.\033[0m \n")

    elif travel_direction == "d" or travel_direction == "i":
        if new_player.items == None:
            print("You have nothing in your inventory")
        else:
            print(f"\nYou have:")
            for count, item in enumerate(new_player.items, 1):
                print(count, item)
            dropSomething = input(
                "\nWould you like to drop something (y/n)?: ")
            if dropSomething == "y" or dropSomething == "yes" and len(new_player.items) >= int(option) - 1:
                option = input("\nInput the number of the item to drop: ")
                if len(new_player.items) >= int(option) - 1:
                    try:
                        new_player.current_room.items = new_player.items[int(
                            option) - 1]
                        new_player.dropItem(new_player.items[int(option) - 1])
                        print(f"\nyou dropped it!\n")
                    except:
                        print("You don't have that item to drop!")

    elif travel_direction == "q":
        exit()
    else:
        print("\nI don't recognize that choice.  You can enter a direction, 'i' for inventory or 'q' to quit.  Try again!\n")
