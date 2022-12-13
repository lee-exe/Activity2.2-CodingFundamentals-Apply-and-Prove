import random

num1 = 10
num2 = 40

# includes 10
random_number = random.randint(num1, num2)

global number_of_guesses
number_of_guesses = 3
global success_message
global incorrect_message

print("Welcome to the guessing game!\n"
      "A number between {} and {} have been chosen at random.\n".format(num1, num2) +
      "You have {} chances to guess the correct number.\n".format(number_of_guesses) +
      "Fail to choose the correct number and you fail the game!")


def first_guess():
    guess1 = int(input("Your first guess: "))
    return guess1


def second_guess():
    guess2 = int(input("Second guess: "))
    return guess2


def third_guess():
    guess3 = int(input("Thrid guess: "))
    return guess3


def guess_check():
    success_message  = "Congratulations! You guessed correctly!!"
    incorrect_message  = "Oops. That's not the correct answer. Please try again"

    print(number_of_guesses)
    first_guess()
    if first_guess() == random_number:
        print(success_message)
        exit(0)
    else:
        number_of_guesses -= 1
        print(number_of_guesses)
        print(incorrect_message)

        second_guess()
        if second_guess() == random_number:
            print(success_message)
            exit(0)
        else:
            number_of_guesses -= 1
            print(number_of_guesses)
            print(incorrect_message)

            third_guess()
            if third_guess() == random_number:
                print(success_message)
                exit(0)
            else:
                number_of_guesses -= 1
                print(number_of_guesses)
                print(incorrect_message)

                print("You failed to guess correctly,\n"
                      "the correct number was {}.\n"
                      "Better luck next time!".format(random_number))


guess_check()