from simpleimage import SimpleImage

def main():
    image = SimpleImage('images/karel.png')
    trimmed_img = trim_crop_image(image, 30)
    trimmed_img.show()


def trim_crop_image(original_img, trim_size):
    """
    This function returns a new SimpleImage which is a trimmed and
    cropped version of the original image by shaving trim_sz pixels
    from each side (top, left, bottom, right) of the image. You may
    assume trim_sz is less than half the width of the image.

    Inputs:
        - original_img: The original image to process
        - trim_size: The number of pixels to shave from each side
                   of the original image

    Returns:
        A new SimpleImage with trim_sz pixels shaved off each
        side of the original image
    """
    # TODO: your code here
    # Calculate the new_width and new_height
    # Create a new blank image and send the new values of width and height
    # Iterating the the values of width and height to assign the x and y value the sise to trim
    # Then update the fixel with new values
    # and apply to the image the new values
    # Retutn the image

    new_width = original_img.width - 2*trim_size
    new_height = original_img.height - 2*trim_size
    new_image = SimpleImage.blank(new_width, new_height)

    for x in range(new_width):
        for y in range (new_height):
            old_x = x + trim_size
            old_y = y + trim_size
            original_pixel = original_img.get_pixel(old_x, old_y)
            new_image.set_pixel(x, y, original_pixel)
    return new_image
    


if __name__ == '__main__':
    main()