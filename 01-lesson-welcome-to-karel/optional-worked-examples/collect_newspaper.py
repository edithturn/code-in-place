from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

def main():
    """
    Pick up the newspaper and then return to home
    """
    move_to_the_newspaper()
    pick_beeper()
    return_home()

def move_to_the_newspaper():
    turn_right()
    move()
    turn_left()
    move_3()

def return_home():
    turn_around()
    move_2()
    for i in range(2):
       move()
       turn_right()

def move_3():
    for i in range(3):
        move()

def move_2():
    for i in range(2):
        move()

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program()