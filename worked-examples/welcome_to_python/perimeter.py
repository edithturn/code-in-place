def main():
    perimether = 0
    for i in range(3):
        number = float(input(f"What is the length of side {i + 1}? "))
        perimether += number
    print(f"The perimeter of the triangle is {perimether}")

if __name__ == "__main__":
    main()