import random

secret_number = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input("Guess the number (1-50): "))
    attempts += 1

    if guess == secret_number:
        print("Congratulations! You guessed it!")
        print("Number of attempts:", attempts)
        break

    elif guess > secret_number:
        print("Too high")

    else:
        print("Too low")

    if attempts == 7:
        print("You have used all 7 attempts.")
        print("The secret number was:", secret_number)
        break