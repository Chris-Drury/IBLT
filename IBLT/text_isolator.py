"""
This file is responsable for ioslating any text
from the images enhanced by the image_enhancer

dependancies:
Pillow (PIL)
pytesseract (OCR)
"""

from PIL import Image, ImageDraw, ImageFont
from IBLT import image_enhancer
import pytesseract


def isolate_text(image_path: str):
    """isolate any text within the image

    Keyword arguments:
    image_path -- the relative path of the image under inspection
    """

    # Setup Google's tesseract
    pytesseract.pytesseract.tesseract_cmd \
        = r'C:\Program Files\Tesseract-OCR\tesseract'

    # Grey Scale the image located at image_path
    image, path = greyscaler(image_path)

    # retrieve the text while removing any formatting tags
    image_string = pytesseract.image_to_string(image)
    image_text = list(filter(None, image_string.split("\n")))
    image_words = image_string.split()

    # open the coloured image to be used during box drawing
    coloured_image = Image.open(image_path)

    # determine the location(s) of the detected text
    data = pytesseract.image_to_data(
        image, output_type=pytesseract.Output.DICT)
    n_boxes = len(data['level'])
    for i in range(n_boxes):

        # determine if the detected text is actual text and not whitespace:
        if data['text'][i].strip() in image_words:
            (x, y, w, h) = (
                data['left'][i],
                data['top'][i],
                data['width'][i],
                data['height'][i])

            # draw the text rectangle on the detected image
            drawer = ImageDraw.Draw(coloured_image, 'RGBA')
            drawer.rectangle([(x, y), (x+w, y+h)], None, 'green', width=1)
            # RGB for yellow = (238, 250, 106, 255)

    coloured_image.show()  # show the product

    # determine the path to save the newly edited colour image
    path_no_extension = image_path.split(".", 1)[0]
    extension = image_path.split(".", 1)[1]
    coloured_image_path = path_no_extension + "_textboxes." + extension

    coloured_image.save(coloured_image_path)

    return image_text


def greyscaler(image_path: str):
    """greyscale the image at the path provided

    Keyword arguments:
    image_path -- the relative path of the image to greyscale
    """
    # open the image
    im = Image.open(image_path)

    # convert the image to grayscale for OCR
    grayscaled_image = im.convert('1')
    # grayscaled_image.show()  # display the grayscale image

    # determine the path to save the newly enhanced image
    path_no_extension = image_path.split(".", 1)[0]
    extension = image_path.split(".", 1)[1]
    grayscale_image_path = path_no_extension + "_grayscale." + extension

    # save the grayscale image
    grayscaled_image.save(grayscale_image_path)

    return grayscaled_image, grayscale_image_path


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




