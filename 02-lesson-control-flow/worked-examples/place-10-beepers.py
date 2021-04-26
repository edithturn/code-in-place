from karel.stanfordkarel import *

"""
File: ForLoopWarmup.py
------------------------------
Place 10 beepers.
"""

def main():
    """
    Place 10 beepers on the spot Karel is currently standing on
    """
    for i in range(10):
        put_beeper()

if __name__ == "__main__":
    run_karel_program()