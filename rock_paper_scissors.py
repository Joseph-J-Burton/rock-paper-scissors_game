rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

# rules:
# Rock wins against scissors
# Scissors win against paper
# Paper wins against rock

# put symbols into a list
symb = [rock, paper, scissors]
# ask for player choice
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice <= 2:
    print(f"Your choice:\n {symb[player_choice]}")

    # generate random computer choice
    computer_choice = random.randint(0, 2)
    print(f"The computer chooses:\n {symb[computer_choice]}")

    # determine who wins
    if computer_choice == 0:
        if player_choice == 2:
            print("Computer wins! ")
        elif player_choice == 1:
            print("You win! ")
        else:
            print("It's a tie! ")
    elif computer_choice == 1:
        if player_choice == 0:
            print("Computer wins! ")
        elif player_choice == 2:
            print("You win! ")
        else:
            print("It's a tie! ")
    elif computer_choice == 2:
        if player_choice == 1:
            print("Computer wins! ")
        elif player_choice == 0:
            print("You win! ")
        else:
            print("It's a tie! ")
else:
    print("Invalid option. Game Over!")
