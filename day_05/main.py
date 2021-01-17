#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
new_letters = []
for letter in range(1, nr_letters + 1): # Adding 1 due to range stop
  new_letters.append(letters[random.randint(0, len(letters) - 1)]) # -1, else index out of range

new_symbols = []
for symbol in range(1, nr_symbols + 1): # Adding 1 due to range stop
  new_symbols.append(symbols[random.randint(0, len(symbols) - 1)]) # -1, else index out of range

new_numbers = []
for number in range(1, nr_numbers + 1): # Adding 1 due to range stop
  new_numbers.append(numbers[random.randint(0, len(numbers) - 1)]) # -1, else index out of range

easy_password = new_letters + new_symbols + new_numbers
print(f"This is your new (eazy) password: {''.join(easy_password)}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password = random.sample(easy_password, k = len(easy_password)) # k for numbers of selected character for randomisation 
print(f"This is your new (hard) randomised password: {''.join(hard_password)}")
      
# HINT: Make your life easier by using functions such as random.choice() or random.shuffle() 
