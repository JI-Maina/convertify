import os
from PIL import Image


def compress_image(image_dir, image_name):
    """Compresses a given image and returns its destination"""

    max_width = 1200

    image = Image.open(image_name)

    width, height = image.size

    aspect_ratio = width / height

    new_height = max_width / aspect_ratio

    new_image = image.resize((max_width, round(new_height)))

    filename = os.path.join(image_dir, image_name.split('/')[-1])

    new_image.save(filename, optimize=True, quality=90)

    return True