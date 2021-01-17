from art import logo, vs
from game_data import data
from replit import clear
import random

compare_data = random.choice(data)
against_data = random.choice(data)
current_score = 0
end_of_game = False

while not end_of_game: 
  clear()
  print(logo)

  while compare_data == against_data: 
    against_data = random.choice(data)

  if current_score > 0: 
    print(f"You're right! Current score: {current_score}")
    
  print(f"Compare A: {compare_data['name']}, a {compare_data['description']}, from {compare_data['country']}.")
  print(vs)
  print(f"Against B: {against_data['name']}, a {against_data['description']}, from {against_data['country']}.")
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  if guess == 'a': 
    if compare_data['follower_count'] > against_data['follower_count']: 
      current_score += 1
      compare_data = against_data
      against_data = random.choice(data)
    else: 
      end_of_game = True
  elif guess == 'b':
    if compare_data['follower_count'] < against_data['follower_count']: 
      current_score += 1
      compare_data = against_data
      against_data = random.choice(data)
    else:
      end_of_game = True

clear()
print(logo)
print(f"Sorry, that's wrong. Final score: {current_score}")