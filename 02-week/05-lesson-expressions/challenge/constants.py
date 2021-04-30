"""
An example program with constants. 
Converts feet to total number of inches.
"""

# Number of inches in a foot
INCHES_IN_FOOT = 12

def main():
    # Ask to the user teh value of feet
    feet = float(input("Enter number of feet: "))
    # Multiply feet with INCHES_IN_FOOT which is a constant value
    inches = feet * INCHES_IN_FOOT
    # Print the value of feet in inches
    print("That is", inches, "inches!")

if __name__ == '__main__':
    main()