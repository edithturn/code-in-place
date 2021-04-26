from karel.stanfordkarel import *

"""
File: FiveCorridorsKarel.py
-----------------------
Karel traverse 5 variable length corridors and place beepers at the ends of them if there aren't already beepers there.
"""

def main():
    """
    Five corridors (for loops, while loops, fencepost, if/else)
    """
    for i in range(5):
       check_row()
       put_beeeper_if_not()
       go_next_row()

def check_row():
   while front_is_clear():
     move()

def put_beeeper_if_not():
   if front_is_blocked():
       if no_beepers_present():
           put_beeper()

def go_next_row():
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    if front_is_clear():
        move()
    turn_right()

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()
if __name__ == "__main__":
    run_karel_program()