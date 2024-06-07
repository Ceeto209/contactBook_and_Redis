import sys
import random


print("You get 3 lives!!!\n")

lives = 3
computer_lives = 3

while lives != 0 and computer_lives != 0:
    print(f"Your lifes: {lives} \nComputer lifes: {computer_lives}\n")
    player_choice = input("Enter...\n 1 for Rock\n 2 for Paper\n 3 for Sissors\n\n")
    player = int(player_choice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")

    computer_choice = random.choice("123")

    computer = int(computer_choice)

    if player == 1:
        if computer == 3:
            print("Rock vs Sissors\n You win!!!\n")
            computer_lives -= 1
        elif computer == 2:
            print ("Rock vs Paper\n You lose!!!\n")
            lives -= 1
        elif computer == 1:
            print("Rock vs Rock\n Tie!!!\n")
    elif player == 2:
        if computer == 3:
            print("Paper vs Sissors\n You lose!!!\n")
            lives -= 1
        elif computer == 2:
            print("Paper vs Paper\n Tie!!!\n")
        elif computer == 1:
            print("Paper vs Rock\n You win!!!\n")
            computer_lives -= 1
    elif player == 3:
        if computer == 3:
            print("Sissors vs Sissors\n Tie!!!\n")
        elif computer == 2:
            print ("Sissors vs Paper\n You win!!!\n")
            computer_lives -= 1
        elif computer == 1:
            print("Sissors vs Rock\n You lose!!!\n")
            lives -= 1

if lives == 0:
    print("\n You lost!!!\n")
elif computer_lives == 0:
    print("\n You won!!!\n")