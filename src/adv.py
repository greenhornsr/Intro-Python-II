from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance","North of you, the cave mount beckons", [Item("lantern", "An old, rusty source of low light."),Item("shovel", "A solid way to dig.")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
directions = ["n", "s", "e", "w"]
actions = ["get", "take", "drop", "i", "inventory" "h"] 
# Make a new player object that is currently in the 'outside' room.
player = Player(input("Please enter your name: "),room['outside'])
# * Prints the current room name
print(player.curr_room.name)
# * Prints the current description (the textwrap module might be useful here).
print(player.curr_room.description)

# Write a loop that:
#

# Helper Function
def player_options():
    print(
    """
    =========================OPTIONS============================
    q: Quit Game.
    h: Display Options.
    n/s/e/w: Change Rooms.
    i/inventory: Display Player Inventory.
    get <item>: Put an item from the room in your inventory.
    drop <item>: Drop an item from your inventory in the room.
    ============================================================
    \n\n
    """
    )

while True:
    print(player.curr_room)
    # display items in the room to user.
    player.curr_room.get_room_items()
# * Waits for user input and decides what to do.
    cmd = input("\nWhat would you like to do?").lower().split(" ")
    
    if len(cmd) == 1:
        if cmd[0] in directions:
        # print("location-to", room[player1.curr_room].n_to.name)
            player.move(cmd[0])
        # get player inventory
        elif cmd[0] == "i" or cmd[0] == "inventory":
            player.view_inventory()
        elif cmd[0] == "h":
            player_options()
# If the user enters "q", quit the game.
        elif cmd[0] == "q":
            # Quit game.
            print("Thanks for playing!")
            break
    elif len(cmd) == 2:
        if cmd[0] in actions:
            if cmd[0] == "get" or cmd[0] == "take":
                roomitem =  [item.name for item in player.curr_room.items if item.name == cmd[1]]
                #choose item from available items in room
                if len(roomitem) == 1:
                    # add item to player inventory
                    player.add_item(cmd[1])
                else:
                    print(f"{cmd[1]} isn't in the {player.curr_room.name}.")
            elif cmd[0] == "drop":
                #choose an item to drop in room
                playeritem = [item.name for item in player.inventory if item.name == cmd[1]]
                if len(playeritem):
                    # remove item from player inventory
                    player.drop_item(cmd[1])
                else: 
                    print(f"{cmd[1]} isn't in the {player.name}'s inventory.")
        else:
            print("Not a valid option.  must be 'get' or 'drop' followed by the item.")
# Print an error message if the movement isn't allowed.
    else:
        print("Must enter a valid command.")
#
# If the user enters a cardinal direction, attempt to move to the room there.
