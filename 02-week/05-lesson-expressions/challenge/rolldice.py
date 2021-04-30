"""
Simulate rolling two dice.
Prints results of each roll as well as the total.
"""

import random

# Number of sides on each die to roll
NUM_SIDES = 6

def main():
    # setting seed is useful for debugging
    # random.seed(1)
    # calculate die1 a number between 1 and 6
    die1 = random.randint(1, NUM_SIDES)
    # calculate die2 a number between 1 and 6
    die2 = random.randint(1, NUM_SIDES)
    # Add the two numbers 
    total = die1 + die2
    # Print the values and the total of the sum
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

if __name__ == '__main__':
    main()