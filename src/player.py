# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, start_room):
        self.name = name
        self.curr_room = start_room
        self.inventory = []

    # def __str__(self):
    #     return f"{self.name}, {self.curr_room}"

    def move(self, direction):
        new_room = self.curr_room.get_room_direction(direction)
        if new_room is not None:
            self.curr_room = new_room
            print(self.curr_room)
        else:
            print("You cannot move that direction.")
    
    def view_inventory(self):
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"You are currently carrying {item}.")
        else:
            print("You have nothing in your inventory.")

    def add_item(self, item):
        for roomitem in self.curr_room.items:
            if roomitem.name == item:
                self.curr_room.items.remove(roomitem)
                self.inventory.append(roomitem)
                print(f"{self.name} has found {roomitem.name}!")
        for playeritem in self.inventory:
            print(f"Items left in player inventory: {playeritem}")

    def drop_item(self, dropitem):
        if dropitem in self.inventory:
            dropped_item = self.inventory.remove(dropitem)
            print(f"{self.name} dropped the {dropped_item}.")
            self.curr_room.add_dropped_item(dropped_item)
        else: 
            print(f"{dropitem} not in {self.name}'s inventory.")





