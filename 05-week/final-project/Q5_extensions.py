from simpleimage import SimpleImage
import random
import sys


N_ROWS = 3
N_COLS = 3
PATCH_SIZE = 200
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE

def make_recolored_patch(red_scale, green_scale, blue_scale):
    list = ["img/my_cat.jpg", "img/dog.jpg", "img/fox.jpg", "img/panda.jpg", "img/simba-sq.jpg"]
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



