from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance","North of you, the cave mount beckons", [Item("Lantern", "An old, rusty source of low light."),]),

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
actions = ["get", "drop", "i", "h"] 
# Make a new player object that is currently in the 'outside' room.
player1 = Player(input("Please enter your name: "),room['outside'])
# * Prints the current room name
print(player1.curr_room.name)
# * Prints the current description (the textwrap module might be useful here).
print(player1.curr_room.description)

# Write a loop that:
#

# Helper Function
def player_options():
    print(
    """
    =====================OPTIONS========================
    q: Quit Game.
    h: Display Options.
    n/s/e/w: Change Rooms.
    i: Display Inventory.
    get <item>: Put an item from the room in your inventory.
    drop <item>: Drop an item from your inventory in the room.
    ====================================================
    """
    )

while True:
# Check what items are in the room.
    player1.curr_room.get_room_items()
# * Waits for user input and decides what to do.
    # what_to_do()
    # test = player_action_prompt()
    # print(test)
    cmd = input("What would you like to do?").lower().split(" ")
    
    if len(cmd) == 1:
        if cmd[0] in directions:
        # print("location-to", room[player1.curr_room].n_to.name)
            player1.move(cmd)
# If the user enters "q", quit the game.
        elif cmd[0] == "q":
            # Quit game.
            print("Thanks for playing!")
            break
    elif len(cmd) == 2:
        if cmd[0] in actions:
            if cmd[0] == "get":
                #choose item from available items in room
                pass
            else:
                #choose an item to drop
                pass
        else:
            print("Not a valid option.  must be 'get' or 'drop' followed by the item.")
# Print an error message if the movement isn't allowed.
    else:
        print("Must enter a valid command.")
#
# If the user enters a cardinal direction, attempt to move to the room there.
