
from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./images"  # folder for input images
pathOut = "./editedImages"  # folder for edited images

# Create the 'editedImages' directory if it doesn't exist
if not os.path.exists(pathOut):
    os.makedirs(pathOut)

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # sharpening, BW
    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    # contrast
    factor = 1.5
    enhanced = ImageEnhance.Contrast(edit)
    edit = enhanced.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    # Save the edited image without the leading period in the path
    edit.save(f'{pathOut}/{clean_name}_edited.jpg')
