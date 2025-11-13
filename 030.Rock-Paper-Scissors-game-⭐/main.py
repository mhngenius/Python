# rock, paper, scissors game

import random

options = ("Rock", "Paper", "Scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (Rock, Paper, Scissors): ")

    print(f"Player= {player}")
    print(f"Computer= {computer}")

    if player == computer:
        print("Its a Tie!")
    elif player == 'Rock' and computer == 'Scissors':
        print("You Win!")
    elif player == 'Paper' and computer == 'Rock':
        print("You Win!")
    elif player == 'Scissors' and computer == 'Paper':
        print("You Win!")
    else:
        print("You Lose!")

    if not input("Play again? (y/n): ").lower() == 'y':
        running = False

print("Thanks for playing :)")