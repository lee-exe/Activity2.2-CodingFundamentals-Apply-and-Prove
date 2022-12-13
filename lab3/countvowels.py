vowels = ['a', 'e', 'i', 'o', 'u']

list_length = int(input("How many letters would you like to add? "))

for item in range(list_length):
    item = input('Enter a new letter: ')
    vowels.append(item)

sentence = input("Please enter a sentence / word: ")

for letter in sentence:
    for item in vowels:
        if letter == item:
            print(letter)
