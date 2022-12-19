class cake:
    def __init__(self, name, colour, tiers, toppings, gluten_free):
        self.name = name
        self.colour = colour
        self.tiers = tiers
        self.toppings = toppings
        self.gluten_free = gluten_free

    # function in class must take a parameter 'self'
    def eatCake(self):
        return f"Here, this {self} cake is delicious!"


new_cake = cake("Vanilla", "Vanilla", 2, ["cream", "strawberries"], True)
print(cake.eatCake(new_cake.name))

