"""
This file is responsable to be the main controller for IBLT,
and is responsable for:

1. Enhancing the provided images
2. Isolating the text to translate
3. translating the text
4. stiching the translated text back onto the image

while also saving the images at each step to demonstrate the
functionality for project demos

dependancies:
Pillow (PIL)
googletrans

TO DO:
4. stitch the translated text to the enhanced image

6. we'll need to figure out how to determine the language
    (user input was stated in the proposal), and if we want a simple GUI
"""

from IBLT import image_enhancer, image_fryer, text_isolator, \
    translator, languages, text_stitcher
from PIL import Image

import sys

image_path = 'images/Swedish.png'
correct = None

for i in range(5):
    # Enhance the image and show it
    enhanced_image, enhanced_image_path = image_enhancer.enhance_image(
        image_path, float(i))

    # isolate the text from the image
    raw_text, ioslated_image_path, text_data = \
        text_isolator.isolate_text(enhanced_image_path)
    print(raw_text)
    ans = input("Is this correct? [Y/N]  ")
    if ans.lower() == "y":
        correct = True
        break
    elif ans.lower() != "n":
        print("[Y/N]")

if not correct:
    print("Error: No variants are correct. \n\
                    Shutting down.")
    sys.exit(0)

# get language input from user and retrieve the corresponding langcode
langcode = languages.get_lang_code(input("Enter language: ").lower())
# TODO: this could be done via GUI later

# translate the text
translated_text = translator.text_translator(raw_text, langcode)

print(translated_text)

# stitch the text back onto the image
stitched_image_path = text_stitcher.text_stitcher(translated_text,
                                                  ioslated_image_path,
                                                  text_data)
