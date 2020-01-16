# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        return f"{self.name}\n{self.description}"

    def get_room_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")

    def get_items(self):
        if len(self.items) > 0:
            for item in self.items:
                print(f"{item}")
        else:
            print("nothing in the room")

    
