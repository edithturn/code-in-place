"""
This program loads an image and applies the narok filter
to it by setting "bright" pixels to grayscale values.
"""

from simpleimage import SimpleImage

BRIGHT_THRESHOLD = 153

def  get_pixel_average(pixel):
    color_component =  pixel.red + pixel.red + pixel.blue
    average_component = color_component // 3
    return average_component

def main():
    image = SimpleImage('images/simba-sq.jpg')

    # Apply the filter
    # TODO: your code here
    for pixel in image:
        pixel_average = get_pixel_average(pixel)

        if (pixel_average > BRIGHT_THRESHOLD):
            pixel.red = pixel_average
            pixel.green = pixel_average
            pixel.blue = pixel_average


    image.show()

if __name__ == '__main__':
    main()