import random

print("Welcome to thr HI - LO game")

number = random.randint(1, 100)
guess = 0

while guess != number:
    guess = int(input("Guess a number between 1 & 100:"))
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print(f"Got it! The number is {number}")
