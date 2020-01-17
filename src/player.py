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
                roomitem.on_take()


    def drop_item(self, dropitem):
        for playeritem in self.inventory:
            if playeritem.name == dropitem:
                self.curr_room.items.append(playeritem)
                self.inventory.remove(playeritem)
                playeritem.on_drop()






