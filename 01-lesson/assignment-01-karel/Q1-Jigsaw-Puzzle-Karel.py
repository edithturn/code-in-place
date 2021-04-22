from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""

def main():
    """
    This function will move to Karel to complete the puzzle and Karel will return to its home. 
    Using for to reduce the use of the function move()
    """
    for i in range(2):
     move()
    pick_beeper()
    move()
    turn_left()
    for i in range(2):
      move()
    put_beeper()
    turn_left()
    turn_left()
    for i in range(2):
     move()
    turn_left()
    turn_left()
    turn_left()
    for i in range(3):
     move()
    turn_left()
    turn_left()


if __name__ == '__main__':
    run_karel_program('Puzzle.w')