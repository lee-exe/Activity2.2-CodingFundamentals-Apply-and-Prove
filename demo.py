# Part 1
print("Hello World")

film1 = "Alien"
film2 = "Batman: Mask of the Phantasm"
film3 = "Dog Soldiers"

# Task
print(film1 + "\n" + film2 + "\n" + film3)

# Part 2
# my_name = input("Please enter name: ")
# print("Hello, " + my_name)

# Task

name = input("Please enter your name: ")
drink = input("Please enter a drink type: ")
size = input("Small, Medium, Large? ")
quantity = input("How many? ")
toppings = ["Milk Chocolate Shavings",
            "White Chocolate Shavings",
            "Caramel Nut Flavoured Cookie Crumb Topping",
            "Chocolate Whipped Cream",
            "Single Mocha Drizzle",
            ]


def whipped_cream():
    yes_or_no = input("Whipped Cream? [Yes] or [No]: ")
    if yes_or_no == "Yes":
        return True
    else:
        return False


if whipped_cream():
    whipped = "with whipped cream"
else:
    whipped = "without whipped cream"

statement = "Hello " + name + ", you have ordered " + quantity + ", " + size + " cups of " + drink + ", " + whipped + ". "


def extras():
    any_extras = input("Would you like any extras? [Yes] or [No]: ")
    if any_extras == "Yes":
        for i in toppings:
            print(i + "\n")
        extra = input("Please select from the menu any extras, or write [None] if you change your mind: ")
        new_statement = statement + "For extras, you have ordered " + extra
        print(new_statement)

    else:
        print(statement)


extras()

