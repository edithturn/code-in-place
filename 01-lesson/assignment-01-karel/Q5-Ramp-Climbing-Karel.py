from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""

def main():
    """
    This function will draw a diagonal line with slope 1/2 and put a beeper in the way
    """
    put_beeper()
    while front_is_clear():
        walk()

def walk():
    move()
    move()
    turn_left()
    move()
    put_beeper()
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    run_karel_program('RampKarel1.w')