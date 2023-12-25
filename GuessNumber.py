import random

def guess_the_number():
    print("Welcome to Guess the number GAME!")
    print("I'm thinking of a number between 1 to 100, can you guess it?")

    secret_number = random.randint(1,100)

    for i in range(3):
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("CONGRATULATIONS!!! You guessed the correct number.")
        else:
            print("Try again! Better luck next time.")   

    else:
        print(f"Sorry the correct number was {secret_number}. Better luck next time!")

guess_the_number()