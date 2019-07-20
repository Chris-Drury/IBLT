"""
This file is responsable for stitching text back onto the image
determined in text_isolator

dependancies:
Pillow (PIL)
"""

from PIL import ImageDraw, Image


def text_stitcher(text: list, image_path: str):
    # open the image
    stitched_image = Image.open(image_path)
    # create the drawer
    drawer = ImageDraw.Draw(stitched_image)
    # find where to put text
    bbox = stitched_image.getbbox()
    # get font for the text  TODO
    # fnt = ImageFont.load_default
    # shave list string
    text = str(text)[2:-2]
    # get length of string in pixels (not actually, changes with font size)
    length = len(str(text))*17
    # find x value of where to but text
    xval = bbox[2] - length
    # find y value of where to put text
    # TODO
    # place translated text onto the image
    drawer.text([xval, bbox[3]/2+10], str(text), 'black')  # , fnt)
    # show finished result
    stitched_image.show()
    # determine the path to save the stitched image
    path_no_extension = image_path.split(".", 1)[0]
    extension = image_path.split(".", 1)[1]
    stitched_image_path = path_no_extension + "_stiched." + extension
    # save the stitched image
    stitched_image.save(stitched_image_path)
    return