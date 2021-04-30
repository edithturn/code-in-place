from karel.stanfordkarel import *

"""
File: ForLoopWarmup.py
------------------------------
Put 4 beepers down in a row, starting with Karel's current position.
"""

def main():
    """
    Put beepers in 4 columns
    """
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()

if __name__ == "__main__":
    run_karel_program()