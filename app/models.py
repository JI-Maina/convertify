from app import db

class UploadedImage(db.Model):
    """Represents an image"""
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)


class EditedImage():
    """Represents a mdified image"""