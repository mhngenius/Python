# number guessing game

import random

lowest_number = 1
highest_number = 100
answer=random.randint(lowest_number,highest_number)
guesses = 0
is_running = True

print("NUMBER GUESSING GAME")
print(f"Select a number between {lowest_number} and {highest_number}")

while is_running:
    guess = input("Enter Your Guess: ")
    if guess.isdigit():
        guess=int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print("That number is out of range")
            print(f"please select a number between {lowest_number} and {highest_number}")
        elif guess < answer:
             print("Too Low! try again")
        elif guess > answer:
             print("Too High! try again")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

    else:
        print("Invalid Guess")
        print(f"please select a number between {lowest_number} and {highest_number}")