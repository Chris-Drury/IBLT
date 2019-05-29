"""
This file contains the function required to "fry" the image.
This is not a required part of the final project, and may not be included. 
However, out of the inteset of jokes, this can be used to "deep fry" images and memes

dependancies:
Pillow (PIL)
"""

from PIL import Image, ImageEnhance


def image_fryer(path: str, scaling: float):
    """'fry' the determined image

    Keyword arguments:
    path    -- the relative location of the image to fry
    scaling -- the scaling factor to use on the image when frying
    """

    # retrieve the image
    krabby_patty = Image.open(path)

    # setup the Krabby Patty frier
    frier = ImageEnhance.Contrast(krabby_patty)
    fried_patty = frier.enhance(scaling)

    # determine the path to save the newly fried patty
    path_no_extension, extension = path.split(".", 1)[0], path.split(".", 1)[1]
    enhanced_image_path = path_no_extension + "_fried_by_" + \
        str(scaling) + "x." + extension

    # save the fried patty
    fried_patty.save(enhanced_image_path)

    return fried_patty, enhanced_image_path
