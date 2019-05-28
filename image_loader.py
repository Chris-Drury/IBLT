from PIL import Image, ImageEnhance

im = Image.open("images/DRAKE.png")
# im.show()

enhancer = ImageEnhance.Sharpness(im)
enhanced_image = enhancer.enhance(30.0)
#  enhanced_image.show()
enhanced_image.save("images/DRAKE_enhanced_by_30x.png")

frier = ImageEnhance.Contrast(enhanced_image)
fried_meme = frier.enhance(4.0)
fried_meme.show()
fried_meme.save("images/DRAKE_fried_by_4x.png")

print("we added the image!")