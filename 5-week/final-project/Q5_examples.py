"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random
import sys

PATCH_SIZE = 250
WIDTH =  400
HEIGHT = 400
def main():
    list = ["img/list.png", "img/dictionary.png", "img/control_flow.png"]
    index = random.randint(0, len(list) - 1)
    patch = SimpleImage(list[index])
    patch.show()

if __name__ == '__main__':
    main()



