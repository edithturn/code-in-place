"""
Ask to the user answer adition problems, it will be right if the uer have three right answers
"""

import random

def main():
    count = 0
    while count < 3:
        # Generate random numbers
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        # Ask to the user solve the problem
        print(f"What is {num1} + {num2}")
        # Ask for the result
        answer = input("Your answer: ")
        result = int(num1) + int(num2)
        # If the answer of the user is correct show a message "correct!"
        if int(answer) == result:
            count  += 1
            print(f"Correct! You've gotten {count} correct in a row.")
        else:
            print(f"Incorrect. The expected answer is {result}")
            # Restarting the count in zero
            count = 0
        # If the answer of the user is incorrect, prin the value of the expected value
    print("Congratulations! You mastered addition.")
if __name__ == '__main__':
    main()