def main():
    temp = float(input("Enter temperature in Fahrenheit: "))
    degrees_celsius = (temp - 32) * 5/9
    print(f"Temperature: {temp}F = 24.{degrees_celsius}")


if __name__ == "__main__":
    main()