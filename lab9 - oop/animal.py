class animal:
    def __init__(self, name, colour, legs, diet):
        self.name = name
        self.colour = colour
        self.legs = legs
        self.diet = diet

    def observe(self):
        return f"Omg, I've just seen a {self}"


lion = animal("Lion", "Yellow-Gold", 4, "Carnivore")
flamingo = animal("Flamingo", "Pink", 2, "Crustacean")

# getattr - retrieve attribute value
print(getattr(lion, 'colour'))

# hasattr - boolean, true if attr exists, false if not
print(hasattr(lion, 'david'))
print(hasattr(lion, 'legs'))

# setattr - add new attr to object with value
setattr(lion, 'size', 'large')
print(getattr(lion, 'size'))

# delattr - delete attribute
delattr(lion, 'size')
print(hasattr(lion, 'size'))
