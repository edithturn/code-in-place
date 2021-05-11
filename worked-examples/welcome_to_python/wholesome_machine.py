AFFIRMATION = "I am capable of doing anything I put my mind to."
def main():
    user_input = input("Please type the following affirmation: I am capable of doing anything I put my mind to.\n")
    while user_input != AFFIRMATION:
        print("That was not the affirmation. \n")
        print(f"Please type the following affirmation: {AFFIRMATION} \n")
        user_input = input()
    print("That's right! :)")


if __name__ == "__main__":
    main()