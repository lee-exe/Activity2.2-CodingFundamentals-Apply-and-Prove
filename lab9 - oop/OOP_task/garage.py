from abc import ABC, abstractmethod
class garage(ABC):
    def __init__(self, carId, brand, wheels, topSpeed, colour):
        self.carId = carId
        self.brand = brand
        self.wheels = wheels
        self.topSpeed = topSpeed
        self.colour = colour

    @abstractmethod
    def isElectric(self, electric):
        pass


