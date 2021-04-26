from karel.stanfordkarel import *

"""
File: WhileLoopWarmup.py
------------------------------
Turn left until Karel is facing a wall.
"""

def main():
    """
    Turn left until Karel is facing a wall.
    """
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program()