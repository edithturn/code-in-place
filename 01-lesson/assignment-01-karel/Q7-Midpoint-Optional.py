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
      turn()
      move()
      turn()
      # Drawind Diagonal
      walkDiagonal()
      turn_right()
      # Drwawing vertical
      walkVertical()
      turn_right()
      walkIntersection()
      # Clean beepers on diagonal
      getPositionBeforeClean()
      cleanBeepersDiagonal()
      turn_right()
      walkVertical()
      turn_right()
      # Clean beepers on intersection
      cleanBeepersIntersection()
      turn_left()
      walkVertical()
      turn_left()
      # Position of Karel at the end
      while no_beepers_present():
        move()
      turn_right()
      turn_right()

def walkVertical():
   while front_is_clear():
     move()

def walkIntersection():
  while front_is_clear():
    put_beeper()
    turn_right()
    move()
    if no_beepers_present():
      turn_left()
      move()
      if beepers_present():
        turn_left()
        while front_is_clear():
          move()
          if front_is_blocked():
              put_beeper()
    else:
      turn()
      while front_is_clear():
        move()
        if front_is_blocked():
            put_beeper()

def cleanBeepersIntersection():
  while front_is_clear():
    if beepers_present():
      pick_beeper()
    turn_right()
    move()
    if no_beepers_present():
      turn_left()
      move()

def  getPositionBeforeClean():
  turn_right()
  while front_is_clear():
    move()
  turn()

def cleanBeepersDiagonal():
  while front_is_clear():
    pick_beeper()
    turn_left()
    move()
    turn_right()
    move()    

def walkDiagonal():
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
    run_karel_program('Midpoint.w')