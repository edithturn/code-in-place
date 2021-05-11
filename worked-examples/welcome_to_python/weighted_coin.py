import random

HEAD_PROBABILITY = 0.7

def main():
    flip = random.randint(0,1)
    if flip < HEAD_PROBABILITY:
        print("Heads")
    else:
        print("Tails")

if __name__ == "__main__":
    main()