from karel.stanfordkarel import *

"""
File: Midpoint.py
------------------------
Place a beeper on the middle of the first row.
"""

def main():
    """
    funciton to find the middle of the world and put a beeper in the 4 and 5 cells
    """
    if front_is_clear():
      move()
    if front_is_blocked():
      put_beeper()
      turn()
    else:
      turn_left()
      turn_left()
      move()
      turn()
      walk_diagonal()
      turn_right()
      walk_vertical()
      turn_right()
      walk_intersection()
      clean_beepers()
      clean_walk_diagonal()
      turn_right()
      walk_vertical()
      turn_right()
      clean_walk_intersection()
      turn_left()
      walk_vertical()
      turn_left()
      while no_beepers_present():
        move()
      turn_right()
      turn_right()

def walk_vertical():
   while front_is_clear():
     move()

def walk_intersection():
  while front_is_clear():
        put_beeper()
        turn_right()
        move()
        if no_beepers_present():
          turn_left()
          move()
        else:
          turn()
          while front_is_clear():
            move()
            if front_is_blocked():
                put_beeper()

def clean_walk_intersection():
  while front_is_clear():
        if beepers_present():
          pick_beeper()
        turn_right()
        move()
        if no_beepers_present():
          turn_left()
          move()

def clean_beepers():
  turn_right()
  while front_is_clear():
    move()
  turn()

def clean_walk_diagonal():
  while front_is_clear():
      pick_beeper()
      turn_left()
      move()
      turn_right()
      move()    

def walk_diagonal():
  while front_is_clear():
    put_beeper()
    turn_left()
    move()
    turn_right()
    move()      

def turn_right():
  turn_left()
  turn_left()
  turn_left()

def turn():
  turn_left()
  turn_left()

if __name__ == '__main__':
    run_karel_program('Midpoint3.w')