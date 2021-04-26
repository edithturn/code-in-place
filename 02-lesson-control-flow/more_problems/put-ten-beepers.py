from karel.stanfordkarel import *

"""
File: TensKarel.py
-----------------------
Place 10 beepers in all spots on the bottom row of any sized world.
"""

def main():
    """
    10s across the board
    """
    while front_is_clear():
        put_ten_beepers()
        move()
    put_ten_beepers()

def put_ten_beepers():
    for i in range(10):
        put_beeper()

if __name__ == "__main__":
    run_karel_program('TensKarel1.w')