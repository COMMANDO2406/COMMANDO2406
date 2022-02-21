import math
import os
import random

actual_number = random.randint(1, 100)
value = random.randint(1, 15)

def bruh():
    x = actual_number - value
    print("your hint is:", x)
    question = input("Is the number higher lower or a jackpot")
    print("\n")
    if question == "higher":
        print("You have chosen higher")
        if actual_number > value:
            print("congrats you win. The real number was:", actual_number)
        if actual_number < value:
            print("the value was lower you lose. The real number was:", actual_number)

    if question == "lower":
        print("You have chosen lower")
        if actual_number > value:
            print("You lose the number was higher The number was:", actual_number)
        if actual_number < value:
            print("You have won. The number was:", actual_number)

    if question == "jackpot":
        print("You have chosen the jackpot")
        if actual_number == value:
            print("you have the jakpot")
        if actual_number < value:
            print("you lose the value was:", actual_number)
        if actual_number > value:
            print("you lose the value was:", actual_number)


bruh()

