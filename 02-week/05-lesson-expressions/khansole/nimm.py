"""
TODO: Write a description here
"""
import random

def main():
    # Ask to the user remove 01 or 02 stones while STONEs exist
    stones = 20
    turn = "Player 1"
    print(f"There are {stones} stones left")
    # If stones > 0 , keep playing
    while stones > 0:
        # Asking the stones to remove to the user
        stones_to_remove = int(input(f"{turn} would you like to remove 1 or 2 stones? "))
        # Remove stones by player, player 01 starts
        stones = removing_stones(stones, stones_to_remove, turn)
        # After remove stone, is turn fo the second player
        turn = alternate_turn(turn)
        # validate if we can still printing the stones that left
        if stones <= 0:
            break
        else:
            print(f"\nThere are {stones} stones left")

def removing_stones(stones, stones_to_remove, turn):
    # If stones to remove are grather than stones then Game Over!
    if stones_to_remove > stones:
        print("Game over")
        stones = 0
    else:
        # While stones to remove are different than 01 and 02, then keep asking.
        while stones_to_remove > 2 or stones_to_remove < 1:
           stones_to_remove = int(input("Please enter 1 or 2: "))
    
    # Substract the stones_to_remove
    stones -= stones_to_remove
    # validate if is end of the game
    validate_end_of_game(stones, turn)
    # return stones
    return stones

def validate_end_of_game(stones, turn):
   # When there are no more stones, the last player to take a stone loses
   if stones == 0:
      turn = alternate_turn(turn)
      print(f"\n{turn} wins!")


def alternate_turn(turn):
    # The two players alternate turns.
    if turn == "Player 1":
       turn = "Player 2"
    else:
       turn = "Player 1"
    return turn

if __name__ == '__main__':
    main()