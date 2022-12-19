class calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x+self.y
    def subtract(self):
        return self.x-self.y
    def multiply(self):
        return self.x*self.y
    def divide(self):
        return self.x/self.y
    def power(self):
        return self.x**self.y

def menu():
    print("Menu: ")

def selected_numbers():
    num1 = input("Please enter a number: ")
    num2 = input("Please select a second number: ")
    return int(num1), int(num2)

def selected_op():
    ops = ["Add", "Subtract", "Multiply", "Divide", "Power"]
    i = 0
    for op in ops:
        i += 1
        print(str(i) + ". " + op)
    select = input("Please select an operation: ")
    operation = ops[int(select) - 1]
    return operation

def compute():
    global result
    menu()
    operation = selected_op()
    num1, num2 = selected_numbers()
    solution = calculator(num1, num2)

    if operation == 'Add':
        result = solution.add()
    elif operation == 'Subtract':
        result = solution.subtract()
    elif operation == 'Multiply':
        result = solution.multiply()
    elif operation == 'Divide':
        result = solution.divide()
    elif operation == 'Power':
        result = solution.power()

    return int(result)

print(compute())
