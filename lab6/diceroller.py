import random


def rollSix():
    return random.randint(1, 6)


def rollEight():
    return random.randint(1, 8)


def rollTen():
    return random.randint(1, 10)


print(rollSix())
print(rollEight())
print(rollTen())


def rollDice(num):
    return random.randint(1, num)


print(rollDice(20))





