"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/my_cat.jpg'

def main():
    image = SimpleImage(PATCH_NAME)
    warhols_image = SimpleImage.blank(WIDTH, HEIGHT)
    set_all_patchs(warhols_image)
    warhols_image.show()

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter.
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    '''
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch

# random.uniform => Returns a random float number between a range
def set_all_patchs(warhols_image):
   """
   Iterating the rows and columns, and for each cell we will add a PATH.
   Before add a path we are put a single path into a cell
   """
   for x in range(N_COLS):
      for y in range(N_ROWS):
         patch = make_recolored_patch(random.random()*1.5, random.random()*1.5, random.random()*1.5)
         put_patch(patch, x, y, warhols_image)

def put_patch(patch, start_x, start_y , warhols_image):
   """
   Getting the position of the single pixel in our blank image (warhols_image), then we are filling
   each pixel with the image. This for each pixel in the blank image of size: 222 and 222
   """
   start_x = start_x * PATCH_SIZE
   start_y = start_y * PATCH_SIZE
   
   for x in range (PATCH_SIZE):
      for y in range (PATCH_SIZE):
         pixel = patch.get_pixel(x, y)
         warhols_image.set_pixel(x + start_x, y + start_y, pixel)

if __name__ == '__main__':
    main()



