import random

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

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0,2)
games_images = [rock, paper, scissors]

if 0 <= player <= 2:
  print(games_images[player])
  
  print("Computer chose:")
  print(games_images[computer])

  if player == 0 and computer == 0: 
    print("Draw.")
  elif player == 1 and computer == 1:
    print("Draw.")
  elif player == 2 and computer == 2:
    print("Draw.")
  elif player == 0 and computer == 1:
    print("You lose.")
  elif player == 0 and computer == 2:
    print("You win.")
  elif player == 1 and computer == 0:
    print("You win!")
  elif player == 1 and computer == 2:
    print("You lose.")
  elif player == 2 and computer == 0:
    print("You lose.")
  elif player == 2 and computer == 1:
    print("You win!")
else: 
  print("Invalid input. Start again.\n")

