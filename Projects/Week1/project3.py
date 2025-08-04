# Project 3: Number Guessing Game

# Concepts Used:
# input(), int()
# if-else
# while loop (optional)
# random.randint (if you’re okay using random early)


import random

secret_number = random.randint(1, 10)
attempts = 0

print("Guess the number (between 1 and 10)")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} tries.")
        break
