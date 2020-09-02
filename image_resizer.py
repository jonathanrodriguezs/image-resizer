import os
from PIL import Image


def resize_image(path, new_path, width, height, crop_center=True):
    '''Image resizing and saving to new path'''
    original_image = Image.open(path)
    image = original_image if not crop_center else crop_center_image(
        original_image)
    new_image = image.resize((width, height))
    full_path = os.path.join(new_path, 'icon')
    new_image.save("{}-{}.{}".format(full_path, str(width), 'png'))


def crop_center_image(image, new_width=None, new_height=None):
    '''Crop the center of an image'''
    width, height = image.size  # Get dimensions

    if (new_width is None or new_height is None):
        new_width, new_height = height, height

    left = (width - new_width) / 2
    top = (height - new_height) / 2
    right = (width + new_width) / 2
    bottom = (height + new_height) / 2

    image = image.crop((left, top, right, bottom))

    return image


def generate_icons(image, path, sizes=(32, 57, 76, 96, 128, 228)):
    for size in sizes:
        resize_image(image, path, size, size)
