from flask import Flask
from flask_uploads import UploadSet, IMAGES, configure_uploads

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd9eed75c59d795794daa7129'
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

from convertify import routes