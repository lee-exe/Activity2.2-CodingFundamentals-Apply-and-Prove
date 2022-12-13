ops = ["Add", "Subtract", "Multiply", "Divide", "Power"]


def selected_numbers():
    num1 = input("Please enter a number: ")
    num2 = input("Please select a second number: ")
    return int(num1), int(num2)


def selected_op():
    i = 0
    for op in ops:
        i += 1
        print(str(i) + ". " + op)
    select = input("Please select an operation: ")
    operation = ops[int(select) - 1]
    return operation


def menu():
    print("Menu: ")


def compute():
    menu()
    operation = selected_op()
    print(operation)
    num1, num2 = selected_numbers()

    if operation == 'Add':
        result = num1 + num2
    elif operation == 'Subtract':
        result = num1 - num2
    elif operation == 'Multiply':
        result = num1 * num2
    elif operation == 'Divide':
        result = num1 / num2
    elif operation == 'Power':
        result = num1 ** num2

    return result


print(compute())
