"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""
import random 

def main():
    # Calculate two random number 
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    # Print two random numbers between 10 and 99 as an adition
    print(f"What is {num1} + {num2}")
    # Ask the user type the result
    answer = input("Your answer: ")
    result = int(num1) + int(num2)
    # If the answer type for th user is correct show a message "correct!"
    if int(answer) == result:
        print("Correct!")
    else:
        print(f"Incorrect. The expected answer is {result}")
    # If the answer type for the user is incorrect, prin the value of the expected value

if __name__ == '__main__':
    main()