"""
This file is responsable for stitching text back onto the image
determined in text_isolator

dependancies:
Pillow (PIL)
"""

from PIL import ImageDraw, Image


def text_stitcher(text: list, image_path: str, tesseract_data):
    # open the image
    stitched_image = Image.open(image_path)
    # create the drawer
    drawer = ImageDraw.Draw(stitched_image)

    txtIdx = 0

    for i in range(len(tesseract_data['level'])):
        if tesseract_data['text'][i] != 'TOMBSTONE':
            (x, y, w, h) = (
                tesseract_data['left'][i],
                tesseract_data['top'][i],
                tesseract_data['width'][i],
                tesseract_data['height'][i])
            drawer.rectangle([(x, y), (x+w, y+h)], 'white', None)
            drawer.text([tesseract_data['left'][i],
                        tesseract_data['top'][i]],
                        text[txtIdx], 'black')
            txtIdx = txtIdx + 1

    path_no_extension = image_path.split(".", 1)[0]
    extension = image_path.split(".", 1)[1]
    stitched_image_path = path_no_extension + "_stiched." + extension
    # save the stitched image
    stitched_image.save(stitched_image_path)
