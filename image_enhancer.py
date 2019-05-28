"""
This file contains the function required to enhance the image before 
retrieving the text from the provided image

dependancy: 
Pillow (PIL) from pypi
"""
from PIL import Image, ImageEnhance


def enhance_image(path: str, scaling: float):
    im = Image.open(path)
    # im.show()

    # create the enhancer and apply the enhancement
    enhancer = ImageEnhance.Sharpness(im)
    enhanced_image = enhancer.enhance(scaling)

    # determine the path to save the newly enhanced image
    path_no_extension, extension = path.split(".", 1)[0], path.split(".", 1)[1]
    enhanced_image_path = path_no_extension + "_enhanced_by_" + str(scaling) + "." + extension

    # save the enhanced image with the new path
    enhanced_image.save(enhanced_image_path)

    return enhanced_image, enhanced_image_path


test, enhanced_image_path = enhance_image("images/DRAKE.png", 5.0)
test.show()

# frier = ImageEnhance.Contrast(enhanced_image)
# fried_meme = frier.enhance(4.0)
# fried_meme.show()
# fried_meme.save("images/DRAKE_fried_by_4x.png")

print("we added the image!")