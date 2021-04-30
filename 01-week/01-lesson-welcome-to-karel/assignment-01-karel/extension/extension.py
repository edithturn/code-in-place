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
    draw_world()
    turn_left()
    move_2()
    get_points()

def get_points():
    pick_beeper()
    turn_left()
    while front_is_clear():
      move()
      if beepers_present():
          pick_beeper()
    turn_right()
    move()
    pick_beeper()
    turn_left()
    move_3()
    pick_beeper()
    for i in range(2):
        move()
    turn_left()
    move()
    pick_beeper()
    turn_right()
    move_2()
    while front_is_clear():
        move()
        if beepers_present():
            pick_beeper()
    pick_beeper_right()
    turn_left()
    move_3()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    move()
    pick_beeper_left()

def pick_beeper_right():
    turn_right()
    move()
    pick_beeper()

def pick_beeper_left():
   turn_left()
   move()
   pick_beeper()

def draw_world():
    paint_corner(ORANGE)
    draw_green_small_block()
    turn_left()
    for i in range(3):
      if front_is_clear():
         move()
         paint_corner(ORANGE)
    move()
    paint_corner(CYAN)
    move()
    turn_left()
    draw_big_red_block()
    turn_left()
    for i in range(3):
        move()
        paint_corner(GREEN)
    for i in range(3):
        move()
        paint_corner(ORANGE)
    draw_gig_yellow_block()
    for i in range(3):
       move()
       paint_corner(GRAY)
    turn_left()
    draw_small_red_block()
    turn_around()
    move()
    turn_left()
    draw_green_big_block()
    for i in range(4):
      paint_corner(ORANGE)
      if front_is_clear():
        move()
    paint_corner(ORANGE)

def draw_small_red_block():
    for i in range(2):
        paint_corner(RED)
        if front_is_clear():
            move()

def draw_big_red_block():
   for i in range(3):
      paint_corner(RED)
      if front_is_clear():
        move()
   turn_around()
   for i in range(2):
      move()

def draw_green_big_block():
   for i in range(3):
      move()
      paint_corner(GREEN)
   turn_left()
   for i in range(2):
      move()
      paint_corner(GREEN)
   turn_around()
   move_2()
   turn_left()
   for i in range(2):
      move()
      paint_corner(GREEN)

def draw_green_small_block():
   for i in range(2):
      move()
      paint_corner(ORANGE)
   move()
   turn_left()
   move()
   turn_around()
   for i in range(2):
      paint_corner(GREEN)
      if front_is_clear():
         move()

def move_2():
   for i in range(2):
       move()

def move_3():
   for i in range(3):
       move()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()   

def draw_gig_yellow_block():
   for i in range(3):
      move()
      paint_corner(CYAN)    
      turn_left()
      move()
      paint_corner(YELLOW)
      turn_around()
      move()
      turn_left() 

if __name__ == "__main__":
    run_karel_program('Midpoint8.w')