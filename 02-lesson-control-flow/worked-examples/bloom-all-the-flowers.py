from karel.stanfordkarel import *

"""
File: SpringFlowers.py
------------------------------
Karel starts in the bottom left corner of a world with 2 empty flower stems, facing East.
Karel should bloom both flowers with beepers and end in the bottom right corner of the world facing East.
"""

def main():
    """
    Spring flowers, Milestone 4
    """
    for i in range(2):
      while front_is_clear():
         move()
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
    run_karel_program('SpringFlowers2.w')