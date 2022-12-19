# Abstract class it most inherit Abstract functionality

from abc import ABC, abstractmethod
class animal(ABC):
    # can't create object from abstract classes. no need for constructor
    size = 0
    type = ""

    @abstractmethod     # Descriptor telling python function is abstract
    def rest(self, hours):
        pass    # Every child MUST INCLUDE the function rest(self, hours). pass = does nothing


class cat(animal):
    def __init__(self, fur_colour, fav_food):
        self.fur_colour = fur_colour
        self.fav_food = fav_food

    # Overriding abstract method
    def rest(self, hours):
        return f"Sleeps for {hours}"    # Comment out

zaph = cat("Browny, black, begie", "tuna")
