from karel.stanfordkarel import *

"""
File: ClimbStem.py
------------------------------
Karel will climb a "stem" -- Karel should start facing a wall. Karel will turn and scale the wall until there is no more wall to Karel's right.
"""

def main():
    """
    Spring flowers, Milestone 2b
    """
    for i in range(4):
        if front_is_clear():
           move()
        else:
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