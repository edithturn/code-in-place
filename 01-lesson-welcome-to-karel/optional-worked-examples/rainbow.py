from karel.stanfordkarel import *

"""
File: Rainbow.py
------------------------------
Karel makes a rainbow!
"""

def main():
    """
    Karel will paint a rimbow
    """
    paint_corner(RED)
    move()
    paint_corner(ORANGE)
    move()
    paint_corner(YELLOW)
    move()
    paint_corner(GREEN)
    move()
    paint_corner(BLUE)
    move()

if __name__ == "__main__":
    run_karel_program()