"""
Simulate rolling two dice, three times.
Prints the results of each die roll.
This program is used to show how variable scope works.
"""

import random

# Number of sides on each die to roll
NUM_SIDES = 6

# Simulates rolling two dice and prints their total
def roll_dice():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print("Total of two dice:", total)

def main():
    # Can set the seed to get the same sequence of random numbers on each run
    # random.seed(1)
    # Seting the value of die1
    die1 = 100
    # Print the value of die1
    print("die1 in main() starts as: " + str(die1))
    # call 03 times roll_dice function
    roll_dice()
    roll_dice()
    roll_dice()
    # Pritning the value of die1
    print("die1 in main() is: " + str(die1))

if __name__ == '__main__':
    main()