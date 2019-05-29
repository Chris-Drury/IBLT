"""
This file is responsable for ioslating any text
from the images enhanced by the image_enhancer

dependancies:
Pillow (PIL)
pytesseract (OCR)
"""

from PIL import Image
from IBLT import image_enhancer


def ioslate_text(image_path: str):
    """ioslate any text within the image

    Keyword arguments:
    image_path -- the relative path of the image under inspection
    """
    # load the image
    im = Image.open(image_path)

    # convert the image to grayscale for OCR
    grayscale_im = im.convert('1')
    grayscale_im.show()  # display the grayscale image

    # determine the path to save the newly enhanced image
    path_no_extension = image_path.split(".", 1)[0]
    extension = image_path.split(".", 1)[1]
    grayscale_image_path = path_no_extension + "_grayscale." + extension
  
    # save the grayscale image
    grayscale_im.save(grayscale_image_path)

    return "Hello World"
