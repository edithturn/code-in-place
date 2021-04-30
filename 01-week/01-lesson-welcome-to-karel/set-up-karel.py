from karel.stanfordkarel import *

"""
File: StepUp.py
--------------------
Karel should pick up the beeper and put it on the ledge
"""

def main():
    """
    Funciton wil move Karel and pick up the beeper until the end of the world, if Karel find a wall its will jump.
    """
    while front_is_clear():
       move()
       if beepers_present():
          pick_beeper()
    if front_is_blocked():
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
        move()
        put_beeper()
        move()


if __name__ == "__main__":
    run_karel_program('StepUp.w')

