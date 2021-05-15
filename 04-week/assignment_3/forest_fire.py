from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.0
DEFAULT_FILE = 'images/greenland-fire.png'

def find_flames(filename):
    """
    This function should highlight the "sufficiently red" pixels
    in the image and grayscale all other pixels in the image
    in order to highlight areas of wildfires.
    """
    image = SimpleImage(filename)
    for pixel in image:
        average = (pixel.red + pixel.blue + pixel.green )//3
        # Here I will apply this avera to the image | I am not sure, helpp!!! Lets see 
        if pixel.red >= average*INTENSITY_THRESHOLD:
            pixel.red = 255
            pixel.blue = 0
            pixel.green = 0
        else:
            # convert to grayscale = average
            pixel.red = average
            pixel.blue = average
            pixel.green =average
    return image

def main():
    filename = get_file()
    image = SimpleImage(filename)

    # Show the original fire   
    original_fire = SimpleImage(filename)
    original_fire.show()

    # Show the highlighted fire
    highlighted_fire = find_flames(filename)
    highlighted_fire.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()