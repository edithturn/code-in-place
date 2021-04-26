from karel.stanfordkarel import *

"""
File: LabyrinthKarel.py
------------------------------
Karel solves labyrinths!
"""

def main():
    """
    Labyrinth (while loops, if/else)
    """
    
    while front_is_clear():
       while front_is_clear():
          move()
       find_direction()

def find_direction():
    if left_is_clear():
        turn_left()
    if right_is_clear():
        turn_right()

def turn_right():
    for i in range(3):
       turn_left()

if __name__ == "__main__":
    run_karel_program('Labyrinth1')