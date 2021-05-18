"""
This program takes an image and generates a reflection.
The top half of the generated image is the same as the original.
The bottom half is the mirror reflection of the top half.

Write a function that returns an output image that is twice the height of the original.
The top half of the output image should be identical to the original image. The bottom half, 
however, should look like a reflection of the top half. The highest row in the top half 
should be “reflected” to be the lowest row in the bottom half. This results in a cool effect.
"""
'''
def mirror_image(filename): 
   """
   Reads image from file specified by filename. 
   Returns a new image that includes the original image 
   and its mirror reflection.   
   """
   
   image = SimpleImage(filename)
   width = image.width
   height = image.height 

   # Create new image to contain mirror reflection
   mirror = SimpleImage.blank(width * 2, height)
   new_image = SimpleImage.blank(width, height*2)
  for y in range(height): 
     for x in range(width): 
        pixel = image.get_pixel(x,y)
        mirror.set_pixel(x, y, pixel)
        mirror.set_pixel((width * 2) - (x+1), y, pixel)

  return mirror
'''



from simpleimage import SimpleImage

DEFAULT_FILE = 'images/mt-rainier.jpg'

def make_reflected(filename):
    original_image = SimpleImage(filename)
    width = original_image.width
    height = original_image.height
    # TODO: your code here.
    # Create a blank image
        # Double in hight of original iamge , width is the same
    # Iterate the rows original image (x, y)
    # Iterate the colums:
        # get pixels from original image
        # set the pixels for orignal image on top half
        # set the reverse pixels for mirror image on bottom half
    mirror = SimpleImage.blank(width, height*2)
    for x in range(width):
        for y in range(height):
            pixel = original_image.get_pixel(x, y)
            mirror.set_pixel(x, y, pixel)
            mirror.set_pixel(x, (height*2) - (y + 1) , pixel)
    # return the finished image with both top half and bottom half on the blank canvas
    return mirror

def main():
    # Get file and load image
    filename = get_file()

    # Show the original image
    original = SimpleImage(filename)
    original.show()

    # Show the reflected image
    reflected = make_reflected(filename)
    reflected.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()