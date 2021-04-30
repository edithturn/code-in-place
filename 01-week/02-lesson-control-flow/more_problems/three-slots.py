from karel.stanfordkarel import *

"""
File: SlotsKarel.py
-----------------------
Place 10 beepers in all spots on the bottom row of any sized world.
"""

def main():
    """
    Three slots (for loops, fencepost)
    """
    for i in range(3):
      put_beeper_slot()
      turn_left()
      move()
      turn_right()
      if front_is_clear():
        move()
def put_beeper_slot():
    turn_right()
    move()
    put_beeper()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program('Slots.w')