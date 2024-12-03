import random

random_number = random.randint(1, 100)

is_game_going = True
attept_tracker = 0


def number_guesser_game(number):
    global is_game_going
    if number > random_number:
        print("Too high!")
    elif number < random_number:
        print("Too low!")
    else:
        print(f"You guessed it! You have attempted {attept_tracker} times.")
        is_game_going = False


while is_game_going:
    try:
        input_number = int(
            input(
                "Guess the number between 1 to 100! ",
            )
        )
        if input_number < 1 or input_number > 100:
            print("Enter number between 1 to 100")
            continue
        else:
            number_guesser_game(input_number)
            attept_tracker += 1
    except:
        print("Please enter valid number!")

# PLEASE RUN THE GAME IN TERMINAL. YOU CAN QUIT THE GAME USING "CTRL + Z" IN MAC
