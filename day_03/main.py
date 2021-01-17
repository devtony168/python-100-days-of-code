print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n')
if choice1.lower() == "left": 
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. \nType "wait" to wait for a boat. Type "swim" to swim across. \n')
  if choice2.lower() == "wait":
    choice3 = input("You arrive at the island unharmend. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n")
    if choice3.lower() == "red":
      print("It's a room full of fire. Game Over.\n")
    elif choice3.lower() == "yellow":
      print("You found the treasure! You Win!\n")
    elif choice3.lower() == "blue":
      print("You enter a room of beasts. Game Over.\n")
    else: 
      print("Game Over.\n")
  elif choice2.lower() == "swim":
    print("Attacked by trout. Game Over.\n")
  else: 
    print("Game Over.")
elif choice1.lower() =="right":
  print("You fell into a hole. Game Over.\n")
else: 
  print("Game Over.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
