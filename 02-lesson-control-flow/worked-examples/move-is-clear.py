from karel.stanfordkarel import *

"""
File: IfElseWarmup.py
------------------------------
Move forward once and put a beeper down if Karel isn't facing a wall. 
If Karel is facing a wall, don't move and just put a beeper down.
"""

def main():
    """
    Move if clear
    """
    
    if front_is_clear():
        move()
    put_beeper()

if __name__ == "__main__":
    run_karel_program('FrontClear.w')