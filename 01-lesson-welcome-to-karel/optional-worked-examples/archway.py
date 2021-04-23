from karel.stanfordkarel import *

"""
File: Archway.py
------------------------------
Karel will move up and over the archway.
"""

def main():
    """
    Karel work along the archway
    """
    up_archway()
    move_3()
    down_archway()

def up_archway():
    turn_left()
    move_3()
    turn_right()

def move_3():
   for i in range(3):
       move()

def down_archway():
    turn_right()
    for i in range(4):
        if front_is_clear():
            move()

def turn_right():
   for i in range(3):
      turn_left()

if __name__ == "__main__":
    run_karel_program()