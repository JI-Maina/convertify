from app import ALLOWED_EXTENSIONS

def allowed_file(filename):
    """Checks if uploaded image is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS