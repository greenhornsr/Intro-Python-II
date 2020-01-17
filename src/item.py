

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return(f"Item:\n{self.name}, {self.description}\n\n")