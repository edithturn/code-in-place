"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random
import sys
import pyautogui
import time


N_ROWS = 6
N_COLS = 6
PATCH_SIZE = 220
WIDTH = N_COLS * (PATCH_SIZE)
HEIGHT = N_ROWS * (PATCH_SIZE)
def main():

    pyautogui.position()
    warhols_image = SimpleImage.blank(WIDTH, HEIGHT)
    set_all_patchs(warhols_image)
    warhols_image.show()
    time.sleep(5)
    warhols_image.close()
    #warhols_image.show()
    #set_all_patchs(warhols_image)
    

def make_recolored_patch(red_scale, green_scale, blue_scale):
    list = ["img/dog.jpg", "img/fox.jpg", "img/panda.jpg", "img/my_cat.jpg", "img/simba-sq.jpg"]
    index = random.randint(0, len(list) - 1)
    print(list[index])

    patch = SimpleImage(list[index])
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch

# random.uniform => Returns a random float number between a range
def set_all_patchs(warhols_image):
    for x in range(N_COLS):
        for y in range(N_ROWS):
            patch = make_recolored_patch(random.random()*1.7, random.random()*1.7, random.random()*1.7)
            put_patch(patch, x, y, warhols_image)

def put_patch(patch, start_x, start_y , warhols_image):
   start_x = start_x * PATCH_SIZE
   start_y = start_y * PATCH_SIZE
   
   for x in range (PATCH_SIZE):
      for y in range (PATCH_SIZE):
         pixel = patch.get_pixel(x, y)
         warhols_image.set_pixel(x + start_x, y + start_y, pixel)

if __name__ == '__main__':
    main()



