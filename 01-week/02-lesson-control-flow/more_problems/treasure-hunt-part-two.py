from karel.stanfordkarel import *

"""
File: TreasureHunt2.py
------------------------------
Karel will move forward until a beeper.
At every beeper, Karel will turn left and move until the next beeper, until Karel is standing on the treasure, which is a pile of 10 beepers.
"""

def main():
    """
    Treasure hunt, part 2
    """
    while no_beepers_present():
        move_to_the_beeper()
        pick_beeper_in_way()
        if left_is_clear():
          turn_left()
        else:
          turn_right()
    while beepers_present():
        pick_beeper()
        
def pick_beeper_in_way():
    pick_beeper()

def move_to_the_beeper():
  while no_beepers_present():
     move()


def turn_right():
   for i in range(3):
     turn_left()

if __name__ == "__main__":
    run_karel_program()