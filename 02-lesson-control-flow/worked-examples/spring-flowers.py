from karel.stanfordkarel import *

"""
File: MoveToWall.py
------------------------------
Karel will move until front is blocked by a wall.
"""

def main():
    """
    Spring flowers, Milestone 2a
    """
    climbing_stem()
    turn_right()
    move()
    go_down_stem()

def go_down_stem():
   turn_right()
   move()
   while front_is_clear():
      move()
   turn_left()

def climbing_stem():
   turn_left()
   while right_is_blocked():
       move()
   


def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program()