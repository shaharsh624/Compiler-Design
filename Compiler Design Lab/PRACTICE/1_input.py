import random

def guess_the_number():
    secret_number = random.randint(1, 10)

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 10")

    for _ in range(3):
        guess = int(input("Your guess : "))

        if guess == secret_number:
            print("Congratulations! You guessed the correct number")
            break
        else:
            print("Wrong guess Try again!")

    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

guess_the_number()
