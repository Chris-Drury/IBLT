"""
This file is responsable for ioslating any text
from the images enhanced by the image_enhancer

dependancies:
Pillow (PIL)
pytesseract (OCR)
"""

from PIL import Image
from IBLT import image_enhancer
import pytesseract


def ioslate_text(image_path: str):
    """ioslate any text within the image

    Keyword arguments:
    image_path -- the relative path of the image under inspection
    """

    # Setup Google's tesseract
    pytesseract.pytesseract.tesseract_cmd \
        = r'C:\Program Files\Tesseract-OCR\tesseract'

    # Grey Scale the image located at image_path
    image, path = greyscaler(image_path)

    # retrieve the text and removing any formatting strings
    image_string = pytesseract.image_to_string(image)
    image_string = image_string.replace("\n", " ")

    return image_string


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