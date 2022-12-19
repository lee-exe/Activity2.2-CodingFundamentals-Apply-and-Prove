from mammal import mammal

class dolphin(mammal):
    def __init__(self, land_or_sea, hair, name, genus, sound):
        super().__init__(land_or_sea, hair)
        self.name = name
        self.genus = genus
        self.sound = sound
    def communication(self):
        return f"A {self.name} {self.sound}s to communicate"

    def antlers(self, yes_no):
        return "No"

snowflake = dolphin("Sea", "none", "Bottlenose Dolphin", "Tursiops", "sqeak")
print(dolphin.communication(snowflake))
