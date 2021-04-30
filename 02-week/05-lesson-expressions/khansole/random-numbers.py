"""
Prints out 10 random numbers between 0 and 100.
"""

import random

NUM_RANDOM = 10
MIN_RANDOM = 0
MAX_RANDOM = 100

def main():
    # print the value of a ten random number between 0 and 100 ( "+1" inclusive)
    for i in range(NUM_RANDOM):
        print(random.randint(MIN_RANDOM, MAX_RANDOM + 1))

if __name__ == '__main__':
    main()