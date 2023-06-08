from PIL import Image
import os
import time


def create_image_set(image_dir, image_name):
    """Returns an image set of different dimension"""

    start = time.time()

    thumb = 30, 30
    small = 540, 540
    medium = 768, 786
    large = 1080, 1080
    xl = 1200, 1200

    img_ext = image_name.split('.')[-1]
    img_name = image_name.split('.')[0]

    image = Image.open(os.path.join(image_dir, image_name))

    # create thumbnail img
    thumbnail_img = image.copy()
    thumbnail_img.thumbnail(thumb, Image.LANCZOS)
    thumbnail_img.save(f"{os.path.join(image_dir, img_name)}-thumbnail.{img_ext}", optimize=True, quality=95)

    # create small img
    small_img = image.copy()
    small_img.thumbnail(small, Image.LANCZOS)
    small_img.save(f"{os.path.join(image_dir, img_name)}-540.{img_ext}", optimize=True, quality=95)

    # create medium img
    medium_img = image.copy()
    medium_img.thumbnail(medium, Image.LANCZOS)
    medium_img.save(f"{os.path.join(image_dir, img_name)}-768.{img_ext}", optimize=True, quality=95)

    # create large img
    large_img = image.copy()
    large_img.thumbnail(large, Image.LANCZOS)
    thumbnail_img.save(f"{os.path.join(image_dir, img_name)}-1080.{img_ext}", optimize=True, quality=95)

    # create thumbnail img
    xl_img = image.copy()
    xl_img.thumbnail(xl, Image.LANCZOS)
    xl_img.save(f"{os.path.join(image_dir, img_name)}-1200.{img_ext}", optimize=True, quality=95)

    end = time.time()

    time_elapsed = end - start

    print(f"Task completed in {time_elapsed}")

    return True