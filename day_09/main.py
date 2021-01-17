from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program!")

bidders = {}

def add_bid():
  name = input("What is your name? ") # Key
  bid = int(input("What is your bid? $")) # Value
  bidders[name] = bid

add_bidders = True
add_bid()
while add_bidders: 
  result = input("Are there any other bidders? Enter 'yes' or 'no': ")
  if result == "no": 
    add_bidders = False
    clear()
  elif result == "yes":
    add_bidders = True
    clear()
    add_bid()
  else: 
    input("Invalid input. Press enter to continue. ")
    clear()

highest_bid = 0    
winner_name = ""
for name in bidders: 
  if bidders[name] > highest_bid: 
    highest_bid = bidders[name]
    winner_name = name

print(f"The winner is {winner_name} with a bid of ${highest_bid}!")