from karel.stanfordkarel import *

"""
File: IfElseWarmup.py
------------------------------
If Karel is facing a wall, put a beeper down, turn left, and move forward. If not, do nothing.
"""

def main():
    """
    Turn signal
    """
    if front_is_blocked():
        put_beeper()
        turn_left()
        move()

if __name__ == "__main__":
    run_karel_program('FrontClear.w')