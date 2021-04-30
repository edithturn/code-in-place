from karel.stanfordkarel import *

"""
File: MoveBeeper.py
------------------------------
Karel will move the beeper up to the top of its column.
Karel starts in the bottom left corner, facing East, in front of the beeper, and Karel will end in the top right corner facing East.
"""

def main():
    """
    Karel will move the beeper on the top of the world
    """
    move()
    pick_beeper()
    turn_left()
    for i in range(2):
        move()
    put_beeper()
    turn_right()
    move()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program()