from abc import ABC, abstractmethod
class mammal(ABC):
    def __init__(self, land_or_sea, hair):
        self.land_or_sea = land_or_sea
        self.hair = hair

    @abstractmethod
    def antlers(self, yes_no):
        pass

    def eat(self):
        return "*eating sounds*"
