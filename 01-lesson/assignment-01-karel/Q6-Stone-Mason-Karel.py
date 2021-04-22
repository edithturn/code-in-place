from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""

def main():
    """
    This function will complete the wall in a building avenue per avenue
    """
    while front_is_clear():
        fill_avenue()
        cross_button_avenue()
    fill_avenue()
    turn_left()

def fill_avenue():
    turn_left()
    just_move()
    turn_around()
    put_beepers()

def just_move():
    if no_beepers_present():
      put_beeper()
    while front_is_clear():
        move()
        
def turn_around():
    turn_left()
    turn_left()

def put_beepers():
  while front_is_clear():
    if no_beepers_present():
       put_beeper()
    move()

def cross_button_avenue():
  turn_left()
  if front_is_clear():
    for i in range(4):
       move()
  if no_beepers_present():
    put_beeper()          

if __name__ == '__main__':
    run_karel_program('SampleQuad2.w')