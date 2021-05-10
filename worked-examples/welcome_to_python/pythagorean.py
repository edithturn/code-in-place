import math

def main():
    lengthAB = int(input("Enter the length of AB "))
    lengthAC = int(input("Enter the length of AC "))
    result = math.sqrt(lengthAB*lengthAB + lengthAC*lengthAC)

    print(f"The length of BC (the hypotenuse) is: {result}")

if __name__ == "__main__":
    main()