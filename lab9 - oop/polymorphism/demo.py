# PolyMorphism
# Poly - Multiple / Many
# Morphism - Can manipulate
# Objects -

class garage:
    def __init__(self, carId, brand, wheels, topSpeed, colour):
        self.carId = carId
        self.brand = brand
        self.wheels = wheels
        self.topSpeed = topSpeed
        self.colour = colour

class car(garage):
    def __init__(self, carId, brand, wheels, topSpeed, colour, model, doors):
        super().__init__(carId, brand, wheels, topSpeed, colour)
        self.model = model
        self.doors = doors

    def setColour(self, newColour):
        colourList = ["Purple", "White", "Cyan", "Green", "Violet", "Red"]
        if newColour in colourList:
            self.colour = newColour
            return f"Colour changed to {newColour}"
        else:
            return "Colour not in colour list."


car1 = car(1, "BMW", 4, 187, "Black", "i8", 2)
car2 = car(2, "McLaren", 4, 220, "Black", "P1", 2)
car3 = car(3, "Mercedes", 4, 200, "Silver", "CLK Black", 2)

# Polymorphism means objects can take on multiple forms

vehicleList = [car1, car2, car3]
# Polymorphism because vehicle can be car1, car2, car3
# Object can take on multiple forms
for vehicle in vehicleList:
    print(vehicle.colour)

