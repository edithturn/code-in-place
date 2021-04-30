from karel.stanfordkarel import *

"""
File: UpstairsDownstairs.py
------------------------------
Karel will climb three stair steps up and then three stair steps down.
"""

def main():
    """
    Upstairs, downstairs (for/while loops)
    """
    for i in range(3): 
       walk_a_step_up()
    move()
    for i in range(3):
      walk_a_step_down()

def walk_a_step_up():
    turn_left()
    move()
    turn_right()
    move()

def turn_right():
   for i in range(3):
      turn_left()

def turn_around():
   for i in range(2):
      turn_left()

def walk_a_step_down():
    turn_right()
    move()
    turn_left()
    if front_is_clear():
       move()
    

if __name__ == "__main__":
    run_karel_program('UpstairsDownstairs.w')