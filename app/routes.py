import os
import secrets
from werkzeug.utils import secure_filename
from flask import render_template, url_for, flash, redirect, send_from_directory, request

from app import app, photos, q
from app.forms import RegistrationForm, LoginForm, UploadForm
from app.modules.allowed import allowed_file
from app.modules.convert import convert_img
from app.tasks import create_image_set


@app.route("/")
def home():
    """Renders site homepage"""
    return render_template('home.html')


@app.route("/convert", methods=['GET', 'POST'])
def convert():
    """returns site homepage"""
    if request.method == 'POST':
        # check if the post request has the file part
        if 'img' not in request.files:
            flash('No file part')
            return "No image uploaded", 400

        file = request.files['img']
        operation = request.form['operation']

        # If the user does not select a file, the browser submits an empty file.
        if file.filename == '':
            flash('No selected file')
            return "No image uploaded", 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            print(filename)
            print(operation)

            # convert according to passed operation
            newfile = convert_img(filename, operation)

            return f"Your file has been converted, get it <a href='url_for({newfile})'>here</a>"

    return render_template('convert.html')


@app.route("/resize", methods=['GET', 'POST'])
def resize():
    """represents site homepage"""

    message = None

    if request.method == "POST":

        image = request.files['image']

        img_dir_name = secrets.token_hex(4)

        img_dir = os.path.join(app.config['UPLOAD_FOLDER'], img_dir_name)
        img_name = secure_filename(image.filename)

        os.mkdir(img_dir)

        image.save(os.path.join(img_dir, img_name))

        q.enqueue(create_image_set, img_dir, img_name)

        flash("Image uploaded successful, wait as we resize it", 'success')

        message = f"/image/{img_dir_name}/{img_name.split('.')[0]}"

    return render_template('resize.html', message=message)


@app.route("/uploads/<filename>")
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)


@app.route('/compress', methods=["GET", "POST"])
def compress():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file', filename=filename)
    else:
        file_url = None
    
    return render_template('compress.html', form=form, file_url=file_url)


@app.route("/register", methods=["GET", "POST"])
def register():
    """displays users registration page"""
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    """Displays users login page"""
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'jomo@tisini.co.ke' and form.password.data == 'password':
            flash('Successfully Logged In', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Invalid password or email', 'danger')
    return render_template('login.html', form=form)


# With database idea
# @app.route("/compress", methods=['GET', 'POST'])
# def compress():
#     """represents site homepage"""
#     if request.method == 'POST':
#         pic = request.files['pic']
#         if not pic:
#             return "No image uploaded", 400
        
#         filename = secure_filename(pic.filename)
#         mimetype = pic.mimetype

#         img = UploadedImage(image=pic.read(), name=filename, mimetype=mimetype)

#         db.session.add(img)
#         db.session.commit()

#         return "Image successfully uploaded", 200
#     return render_template('compress.html')


# form = UploadForm()
#     if form.validate_on_submit():
#         filename = photos.save(form.photo.data)
#         file_url = url_for('get_file', filename=filename)
#     else:
#         file_url = None