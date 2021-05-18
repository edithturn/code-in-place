from simpleimage import SimpleImage

def main():
    image = SimpleImage('images/simba-sq.jpg')
    bordered_img = add_border(image, 10)
    bordered_img.show()


def add_border(original_img, border_size):
    """
    This function returns a new SimpleImage which is the same as
    original image except with a black border added around it. The
    border should be border_size many pixels thick.

    Inputs:
        - original_img: The original image to process
        - border_size: The thickness of the border to add around the image

    Returns:
        A new SimpleImage with the border added around original image
    """
    # TODO: your code here
    new_width = original_img.width + 2*border_size
    new_height = original_img.height + 2*border_size
    new_image = SimpleImage.blank(new_width, new_height)


    for x in range(new_image.width):
        for y in range(new_image.height):
            if is_border_pixel(x, y,  border_size, new_image):
                pixel = new_image.get_pixel(x, y)
                pixel.red = 0
                pixel.blue = 0
                pixel.green = 0
            else:
                old_x = x - border_size
                old_y = y - border_size
                old_pixel = original_img.get_pixel(old_x, old_y)
                new_image.set_pixel(x, y,old_pixel)

    return new_image

def is_border_pixel(x, y, border_size, bordered_img):
    if x < border_size:
        return True
    if x >= bordered_img.width - border_size:
        return True
    if y < border_size:
        return True
    if y >= bordered_img.height - border_size:
        return True

    return False

if __name__ == '__main__':
    main()