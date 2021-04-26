from karel.stanfordkarel import *

"""
File: BloomFlower.py
------------------------------
Karel will scale the stem of the flower she's facing, bloom the flower with 4 beepers, and return to the ground.
Karel should end up in the bottommost row, directly to the right of the stem, facing East.
"""

def main():
    """
    Spring flowers, Milestone 3
    """
    for i in range(4):
      if front_is_clear():
         move()
      else:
         climbing_stem()
         bloom()
         go_down_stem()

def bloom():
   put_beeper()
   for i in range(3):
       move()
       put_beeper()
       turn_right()
   turn_around()

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    for i in range(3):
       turn_left()

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


if __name__ == "__main__":
    run_karel_program()