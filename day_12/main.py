import random
from art import logo

mystery_number = random.randint(1, 101)
attempts = 0
end_of_game = False
difficulty_chosen = False

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
#print(f"Pssst, the correct answer is {mystery_number}")

while not difficulty_chosen: 
	difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
	if difficulty == 'easy':
		attempts = 10
		difficulty_chosen = True
	elif difficulty == 'hard':
		attempts = 5
		difficulty_chosen = True
	else: 
		print("Invalid input. Try again. ")

while not end_of_game: 
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  
  if mystery_number == guess: 
    print(f"You got it! The answer was {mystery_number}!")
    end_of_game = True
  elif guess < 1 or guess > 100: 
	  print("Number out of range. Try again.")
  elif mystery_number > guess: 
    print("Too low.")
    attempts -= 1
  elif mystery_number < guess: 
    print("Too high.")
    attempts -= 1
  else:
	  print("Not a number. Try again.")

  if attempts == 0:
    print("You've run out of guesses, you lose.")
    end_of_game = True
  else: 
    if not mystery_number == guess: 
      print("Guess again.")
