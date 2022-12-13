import random


def rollDie1():
    return random.randint(1, 6)


def rollDie2():
    return random.randint(1, 6)


def rollDie3():
    return random.randint(1, 6)


def rollDie4():
    return random.randint(1, 6)


def fourDieRoll():
    die1 = rollDie1()
    die2 = rollDie2()
    die3 = rollDie3()
    die4 = rollDie4()

    print(die1, die2, die3, die4)

    pool = [die1, die2, die3, die4]
    pool.remove(min(pool))
    summation = sum(pool)

    return summation


print(fourDieRoll())
