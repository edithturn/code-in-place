from karel.stanfordkarel import *

"""
File: IfElseWarmup.py
------------------------------
Invert the spot Karel is currently standing on.
"""

def main():
    """
    Invert spot
    """
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()

if __name__ == "__main__":
    run_karel_program('InvertNoBeeper')