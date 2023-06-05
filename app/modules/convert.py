import os
from PIL import Image, ImageOps
from app import app


def convert_img(filename, operation):
    """Converts an image to a chosen format"""

    print(app.config['UPLOAD_FOLDER'])

    image = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], f'{filename}'))

    print(image.mode)

    if image.mode == 'RGBA':
        image = image.convert('RGB')
    
    print(image.mode)
    
    if operation == "cgray":
        newfile = os.path.join(app.config['UPLOAD_FOLDER'], f'{filename}')
        img_gray = ImageOps.grayscale(image)
        img_gray.save(newfile)
        return newfile
    
    elif operation == "cjpg":
        newfile = os.path.join(app.config['UPLOAD_FOLDER'], f"{filename.split('.')[0] + '.jpg'}")
        image.save(newfile)
        return newfile

    elif operation == "cpng":
        newfile = os.path.join(app.config['UPLOAD_FOLDER'], f"{filename.split('.')[0] + '.png'}")
        image.save(newfile)
        return newfile
    
    elif operation == "cwebp":
        newfile = os.path.join(app.config['UPLOAD_FOLDER'], f"{filename.split('.')[0] + '.webp'}")
        image.save(newfile)
        return newfile
