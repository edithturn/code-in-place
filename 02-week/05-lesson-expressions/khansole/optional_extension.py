"""
Extend Khansole Academy, this game will make calculations of a number depending if it is even or odd, until reach ONE
"""

def main():
    user_input = int(input("Enter a number: "))
    steps_count = 1
    # First time make de calculation and tell me if the number is odd of even
    number = check_number(user_input)
    # Take resulto of the first calculation and keep calculating until reach 1
    while number > 1:
        number = check_number(number)
        steps_count += 1
    print(f"The process took {steps_count} steps to reach 1")

"""Check if the number is Even or Odd and pritn a message with the original number and the rsult after the calculation"""
def check_number(user_input):
    if user_input%2 == 0: # Is Even
       number = user_input//2
       print(f"{user_input} is even, so I take half: {number}")
    else: # Is Odd
       number = 3*user_input + 1
       print(f"{user_input} is odd,  so I make 3n + 1: {number}")
    return number

if __name__ == "__main__":
    main()