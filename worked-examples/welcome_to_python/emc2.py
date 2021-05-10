C = 299792458 

def main():
    number = float(input("Enter kilos of mass: "))
    e = number*(C**2)
    m = number 
    print("e = m*(C**2)...")
    print(f"m = {number} kg")
    print(f"C = {C} m/s")
    print(f"{e} joules of energy!")

if __name__ == "__main__":
    main()