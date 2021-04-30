"""
This program asks the user for a number
and prints its square root.
"""

import math

def main():
    # Ask to the user for a number
    num = float(input("Enter number: "))
    # Claculate the square of the number
    root = math.sqrt(num)
    # Print the answer
    print("Square root of", num, "is", root)

if __name__ == '__main__':
    main()