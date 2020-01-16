from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
    @abstractmethod
    def speak(self):
        pass
    @abstractmethod
    def species(self):
        pass


class Dog(Animal):
    def __init__(self, name, legs=4):
        super().__init__(name, legs)
    def speak(self):
        return "WOOF!"
    def species(self):
        print("Dog")

class Bird(Animal):
    def __init__(self, name, legs=2):
        super().__init__(name, legs)
    def speak(self):
        return "Tweet! Tweet!"
    def species(self):
        print("Bird")

class Cat(Animal):
    def __init__(self, name, legs=4):
        super().__init__(name, legs)
    def speak(self):
        return "Meeeeooooow!"
    def species(self):
        print("Feline")

# Dogs
rover = Dog('Rover')
rover.speak()
fido = Dog('Fido')
fido.speak()

# Birds
tweety = Bird('Tweety')

# Cats
kitty = Cat('Kitty')

animals = [rover, fido, tweety, kitty]

for animal in animals:
    print(f"{animal.name} says {animal.speak()}!")