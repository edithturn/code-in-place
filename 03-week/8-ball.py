import random
"""
Simulates a magic eight ball.
Prompts the user to type a yes or no question and gives
a random answer from a set of prefabricated responses.
"""

ANSWER_1 = "As I see it, yes."
ANSWER_2 = "Ask again later."
ANSWER_3 = "Better not to tell you now."
ANSWER_4 = "Cannot predict now. "
ANSWER_5 = "Concentrate and ask again."
ANSWER_6 = "Don't count on it. "
ANSWER_7 = "It is certain."
ANSWER_8 = "It is decidedly so."
ANSWER_9 = "Most likely."
ANSWER_10 = "My reply is no. "
ANSWER_11 = "y sources say no."
ANSWER_12 = "Outlook not so good."
ANSWER_13 = "Outlook good. "
ANSWER_14 = "Reply hazy, try again."
ANSWER_15 = "Signs point to yes."
ANSWER_16 = "Very doubtful."
ANSWER_17 = "Without a doubt."
ANSWER_18 = "Yes."
ANSWER_19 = "Yes - definitely. "
ANSWER_20 = "You may rely on it."


def main():
    # Asking to the user repeatedly until the question is null, then show and answer
    answer = input("Ask a yes or no question: ")
    while answer != "":
        answer_number = random.randint(1, 20)
        choose_answer(answer_number)
        answer = input("Ask a yes or no question: ")

def choose_answer(choose):
    """
    Thi function will select an asnwer according to the questions choose for the use.
    """
    if choose == 1:
        print(ANSWER_1)
    elif choose == 2:
        print(ANSWER_2)
    elif choose == 3:
        print(ANSWER_3)
    elif choose == 4:
        print(ANSWER_4)
    elif choose == 5:
        print(ANSWER_5)
    elif choose == 6:
        print(ANSWER_6)
    elif choose == 7:
        print(ANSWER_7)
    elif choose == 8:
        print(ANSWER_8)
    elif choose == 9:
        print(ANSWER_9)
    elif choose == 10:
        print(ANSWER_10)
    elif choose == 11:
        print(ANSWER_11)
    elif choose == 12:
        print(ANSWER_12)
    elif choose == 13:
        print(ANSWER_13)
    elif choose == 14:
        print(ANSWER_14)
    elif choose == 15:
        print(ANSWER_15)
    elif choose == 16:
        print(ANSWER_16)
    elif choose == 17:
        print(ANSWER_17)
    elif choose == 18:
        print(ANSWER_18)
    elif choose == 19:
        print(ANSWER_19)
    elif choose == 20:
        print(ANSWER_20)
    else:
        print("I don't have idea! ")

if __name__ == "__main__":
    main()