import random

randomNumber = random.randint(1, 100)
print(randomNumber)

guessedNumbers = []

isGameEnded = True

def game(value):
    number = int(input("Guess a number between 1 and 10: ", ))
    if value == number:
        global isGameEnded
        isGameEnded = False
        guessedNumbers.append(number)
        print(guessedNumbers)
        print(f"Correct! You found the number in {len(guessedNumbers)} guesses.")
    elif number < value:
        guessedNumbers.append(number)
        print("Too low!")
    elif number > value:
        guessedNumbers.append(number)
        print("Too high!")

while isGameEnded:
    game(randomNumber)

