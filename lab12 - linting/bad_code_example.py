"""
Fixing bad code
"""

from random import randint
DICE_ROLLER_NUMBER = 6
def roll_lots_of_dice():
    """
    Rolls random die
    :return:
        random number between 1 and 6
    """
    return randint(1, 6)


print(roll_lots_of_dice())
def roll_lots_of_dice2():
    """
    Rolls random die
    :return:
        random number between 1 and 6
    """
    return randint(1, 10)


def roll_custom_numbers(number1, number2):
    """
    Randomly chooses number
    :return:
        random number between number1 and number2
    """
    return randint(number1, number2)


def check_rolls():
    """
    Rolls random die
    :return:
        random number between 1 and 6
    """

    if roll_lots_of_dice2() >= 6:
        return "big number!!!"
    return "small number :( "


CHECK_ROLLS_VAR = check_rolls()
print(CHECK_ROLLS_VAR)
LONG_VAR_NAME = "this is a really long variable that is integral to the flow of the code, " \
                "if this variable is to " \
                "become any shorter the code will simply fail " \
                "as this is a fundamental piece of code for the really " \
                "important and really resilient code base.. how many chars now?? "
