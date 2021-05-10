SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my " # adjective noun verb

def main():
    s1 = input("Please type an adjective and press enter. ")
    s2 = input("Please type an adjective and press enter. ")
    s3 = input("Please type an adjective and press enter. ")

    print(f"{SENTENCE_START} {s1} {s2} {s3}!")

if __name__ == "__main__":
    main()