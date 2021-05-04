"""
Asks the user for a number until they enter -1
Reports the total value of all the numbers at the end
"""

def main():
   total_sum = 0
   while True:
    user_input = int(input("Type a number: "))
    if user_input == -1:
       break
    else:
       total_sum += user_input
   print(f"total is {total_sum}")

if __name__ == '__main__':
    main()