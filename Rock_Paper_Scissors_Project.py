import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
"""

paper = """ 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """ 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_list = [rock, paper, scissors]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print("You chose: ")
print(game_list[your_choice])
print("Computer chose:")
computer_choice = random.randint(0,2)

print(game_list[computer_choice])

if your_choice == 1 and computer_choice == 0:
      print("You win")
if your_choice == 0 and computer_choice == 2:
      print("You win")

if your_choice == 2 and computer_choice == 1:
      print("you win")

if your_choice == computer_choice:
      print("Its a draw!")

else:
      print("you lose")