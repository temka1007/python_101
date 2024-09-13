import random

x = random.randint(1, 10)

print("Welcome to the number guess game!")
print("Enter number between 1 and 10")
guessedNumber = input("Your number: ")

if x == int(guessedNumber):
    print(x)
    print("Congratulations! You guessed it.")
elif x > int(guessedNumber):
    print(x)
    print("GAME OVER! Too low.")
elif x < int(guessedNumber):
    print(x)
    print("GAME OVER! Too high.")