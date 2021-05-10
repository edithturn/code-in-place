"""
Prints the Fizz Buzz sequence up to a given number.
"""

def main():
    number = int(input("Number to count to: "))
    count_fizzbuzz = 0
    count_buzz = 0
    count_fizz = 0

    for num in range(number + 1):
        if num%5 == 0 and num%3 == 0:
            print("Fizzbuzz")
            count_fizzbuzz += 11
        elif num%5 == 0:
            print("Buzz")
            count_buzz += 1
        elif num%3 == 0:
            print("Fizz")
            count_fizz += 1
        else:
            print(num)
    
    print(f"\nNum Fizzed " + str(count_fizz))
    print(f"Num Buzzed " + str(count_buzz))
    print(f"Num Fizzbuzzed " + str(count_fizzbuzz))
    

if __name__ == '__main__':
    main()