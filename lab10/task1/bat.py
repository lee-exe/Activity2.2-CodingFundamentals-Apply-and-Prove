from mammal import mammal
class bat(mammal):
    def __init__(self, land_or_sea, hair, name, genus, wingspan, diet):
        super().__init__(land_or_sea, hair)
        self.name = name
        self.genus = genus
        self.wingspan = wingspan
        self.diet = diet

    def details(self):
        return f"A {self.name} has a wingspan of {self.wingspan}in.\nThey feed " \
               f"primarily on a diet of {self.diet}."

    def antlers(self, yes_no):
        return "No"

vampire_bat = bat("land", "Yes", "Vampire Bat", "Desmodus", "7", "mammalian blood")
print(bat.details(vampire_bat))
