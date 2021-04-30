from karel.stanfordkarel import *

"""
File: ZigZagKarel.py
-----------------------
Places a zig zag pattern of beepers in the world.
"""

def main():
    """
    Zig zag (while loops, optional if/else)
    """
    zig_zag()
    while front_is_clear():
        return_base()
        inspect_way()
        zig_zag()
    set_face_east()

def set_face_east():
    turn_right()
    move()
    turn_left()

def inspect_way():
    if front_is_clear():
        move()

def zig_zag():
    put_beeper()
    turn_left()
    move()
    turn_right()
    if front_is_clear():
        move()
        put_beeper()

def return_base():
    turn_right()
    move()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program('ZigZag1.w')