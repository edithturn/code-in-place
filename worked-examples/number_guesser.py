import random
"""
Number Guesser Program

This is an example of how to use variables to 
keep track of information in a program that 
also makes use of loops
"""

def main():
    count = 1
    lower = 1
    upper = 100
    num = random.randint(lower, upper)

    while True:
        indicator = input(f"Is your number {num}? ")
    
        if indicator == "correct":
            print(f"I win! It took me {count} guesses")
            break
        else:
            num , new_lower, new_upper = guess_number(num, indicator, lower, upper)
            count += 1
            lower = new_lower
            upper = new_upper
        
def guess_number(num, indicator, lower, upper):
    new_lower = lower
    new_upper = upper

    if indicator == "lower":
       new_upper = num - 1
       num = random.randint(new_lower, new_upper)
    elif indicator == "higher":
       new_lower = num + 1
       num = random.randint(new_lower, new_upper)
    else:
        print("Just type: lower or higher")
    return num, new_lower, new_upper

if __name__ == "__main__":
    main()