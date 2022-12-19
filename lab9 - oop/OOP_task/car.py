from garage import garage
class car(garage):
    def __init__(self, carId, brand, wheels, topSpeed, colour, model, doors):
        super().__init__(carId, brand, wheels, topSpeed, colour)
        self.model = model
        self.doors = doors
    def isElectric(self, electric):
        return True

    '''
    My attempt at getters and setters
    '''
    # My attempt at getter and setter
    # @property
    # def colour(self):
    #     return self.colour
    #
    # @colour.setter
    # def colour(self, newColour):
    #     if isinstance(newColour, str):
    #         pass
    #     else:
    #         raise ValueError("Type must be a string")
    #     self.colour = newColour

    '''
    Reece's getters and setters
    '''

    def setColour(self, newColour):
        colourList = ["Purple", "White", "Cyan", "Green", "Violet", "Red"]
        if newColour in colourList:
            self.colour = newColour
            return f"Colour changed to {newColour}"
        else:
            return "Colour not in colour list."



tesla = car(1, "Tesla", 4, 200, "Red", "Model S", 4)
print(tesla.setColour("White"))
print(tesla.colour)

