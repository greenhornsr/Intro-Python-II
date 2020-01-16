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

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} has found {item}!")
        print(self.inventory)

