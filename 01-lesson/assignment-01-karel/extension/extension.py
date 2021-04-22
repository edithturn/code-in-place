from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""

def main():
    """
    Simulation of movement
    """
    paint_world()
    
def paint_world():
    paint_corner(ORANGE)
    for i in range(2):
        move()
        paint_corner(ORANGE)
    move()
    turn_left()
    move()
    paint_corner(RED)
    turn_left()
    turn_left()
    paint_corner(RED)
    for i in range(2):
        paint_corner(RED)
        if front_is_clear():
            move()
    turn_left()
    for i in range(3):
      if front_is_clear():
         move()
         paint_corner(GREEN)
    for i in range(2):
      if front_is_clear():
        move()
      paint_corner(CYAN)

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

if __name__ == "__main__":
    run_karel_program('Midpoint8.w')