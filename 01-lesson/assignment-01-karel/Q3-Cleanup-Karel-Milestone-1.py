from karel.stanfordkarel import *

"""
File: SafePickup.py
--------------------
When you finish writing this file, Karel should be able to
pick up a beeper from the current position if one is present
(but do nothing if no beepers are present).
"""

def main():
    """
   Checking if beeper is present in the world, if is present then pick up it
    """
    if beepers_present():
        pick_beeper()       


if __name__ == '__main__':
    run_karel_program('SafePickup2.w')