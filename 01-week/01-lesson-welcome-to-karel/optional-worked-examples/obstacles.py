from karel.stanfordkarel import *

"""
File: Obstacles.py
------------------------------
Karel will jump over the obstacles and put beepers in the pink squares.
"""

def main():
    """
    put a beeper in the mittle of the world, jumping the obstacles
    """
    move()
    turn_left()
    for i in range(3):
        collect_beeper()
    turn_right()
    move_2()

def collect_beeper():
   for i in range(2):
     move()
     turn_right()
   move()
   put_beeper()
   turn_around()

def turn_around():
    turn_left()
    turn_left()

def move_2():
    for i in range(2):
        move()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program('Obstacles.w')