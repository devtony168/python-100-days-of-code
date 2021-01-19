import art as a
import random

print(a.logo)
print("Welcome to the Dice Rolling Simulator!")

dice_faces = [a.dice1, a.dice2, a.dice3, a.dice4, a.dice5, a.dice6]

dice_simulator_on = True


def random_dice():
    return random.randint(1, 6)


def roll_dice(num):
    print(dice_faces[num - 1])
    print(f"You rolled: {num}")


def play_again():
    answer = input("Do you want to roll again? Type 'yes' to continue or 'no' to exit: ")
    if answer.lower() == 'no' or answer.lower() == 'n':
        print("Thank you for using Dice Rolling Simulator. See you next time!")
        return False
    elif answer.lower() == 'yes' or answer.lower() == 'y':
        return True
    else:
        print("Invalid input. Quit Dice Rolling Simulator. ")


while dice_simulator_on:
    num = random_dice()
    roll_dice(num)
    dice_simulator_on = play_again()
