import redis
from flask import Flask
from rq import Queue
from flask_uploads import UploadSet, IMAGES, configure_uploads

UPLOAD_FOLDER = '/home/irutu/Alx/convertify/app/uploads'
ALLOWED_EXTENSIONS = {'jpg', 'png', 'jpeg'}

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd9eed75c59d795794daa7129'
app.config['UPLOADED_PHOTOS_DEST'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

r = redis.Redis()
q = Queue(connection=r)

from app import routes
