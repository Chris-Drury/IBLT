"""
This file contains the function required to enhance the image before
retrieving the text from the provided image

dependancies:
Pillow (PIL)
"""

from PIL import Image, ImageEnhance


def enhance_image(path: str, scaling: float):
    """Enhance the determined image

    Keyword arguments:
    path    -- the relative location of the image to enhance
    scaling -- the scaling factor to use on the image when enhancing
    """

    # retireve the image
    im = Image.open(path)

    # create the enhancer and apply the enhancement
    enhancer = ImageEnhance.Sharpness(im)
    enhanced_image = enhancer.enhance(scaling)

    # determine the path to save the newly enhanced image
    path_no_extension, extension = path.split(".", 1)[0], path.split(".", 1)[1]
    enhanced_image_path = path_no_extension + "_enhanced_by_" + \
        str(int(scaling)) + "x." + extension

    # save the enhanced image with the new path
    enhanced_image.save(enhanced_image_path)

    return enhanced_image, enhanced_image_path


# test, enhanced_image_path = enhance_image("images/DRAKE.png", 5.0)
# test.show()

# fried_test, fried_image_path = image_fryer(enhanced_image_path, 20.0)
# fried_test.show()
