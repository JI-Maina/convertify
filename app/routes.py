import os
import secrets
from werkzeug.utils import secure_filename
from flask import render_template, url_for, flash, redirect, send_from_directory, request, send_file

from app import app, photos, q
from app.forms import RegistrationForm, LoginForm, UploadForm
from app.modules.allowed import allowed_file
from app.modules.convert import convert_img
from app.modules.compress import compress_image
from app.tasks import create_image_set


@app.route("/")
def home():
    """Renders site homepage"""
    return render_template('home.html')


@app.route("/uploads/<filename>")
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)


@app.route("/convert", methods=['GET', 'POST'])
def convert():
    """returns site homepage"""
    if request.method == 'POST':
        # check if the post request has the file part
        if 'img' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)

        file = request.files['img']
        operation = request.form['operation']

        # If the user does not select a file, the browser submits an empty file.
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'uploads', filename))

            print(filename)
            print(operation)

            # convert according to passed operation
            newfile = convert_img(filename, operation)

            flash("Your image has been converted", 'success')

    return render_template('convert.html')


@app.route("/resize", methods=['GET', 'POST'])
def resize():
    """represents site homepage"""

    message = None

    if request.method == "POST":

        image = request.files['image']

        img_dir_name = secrets.token_hex(4)

        img_dir = os.path.join(app.config['UPLOAD_FOLDER'], 'resized', img_dir_name)
        img_name = secure_filename(image.filename)

        os.mkdir(img_dir)

        image.save(os.path.join(img_dir, img_name))

        create_image_set(img_dir, img_name)

        flash("Image uploaded successful, wait as we resize it", 'success')

        message = f"/image/{img_dir_name}/{img_name.split('.')[0]}"

    return render_template('resize.html', message=message)


@app.route('/compress', methods=["GET", "POST"])
def compress():
    if request.method == 'POST':
        if 'img' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
        
        image = request.files['img']

        if image.filename == '':
            flash('No image selected for uploading', 'danger')
            return redirect(request.url)
        
        if image and allowed_file(image.filename):
            img_name = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], 'uploads', img_name))
            file_url = url_for('get_file', filename=img_name)

            save_dir = os.path.join(app.config['UPLOAD_FOLDER'], 'compressed')
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'uploads', img_name)

            print(save_dir)
            print(file_path)

            compress_image(save_dir, file_path)

            comp_url = url_for('get_comp', filename=img_name)

            orig_size = round(os.path.getsize(file_path) / 1000, 2)
            comp_size = round(os.path.getsize(os.path.join(save_dir, img_name)) / 1000, 2)

            diff = orig_size - comp_size

            print(orig_size)
            print(comp_size)
            print(diff)

            percent = round((diff / orig_size) * 100)

            flash(f'Image successfully compressed by {percent}%', 'success')

            return render_template('compress.html', file_url=file_url, comp_url=comp_url, filename=img_name, orig_size=orig_size, comp_size=comp_size)
        else:
            flash('Allowed image types are - png, jpg, jpeg', 'warning')
            return redirect(request.url)
    
    return render_template('compress.html')


@app.route('/compressed/<filename>')
def get_comp(filename):
    return send_from_directory(app.config['COMPRESSED_FOLDER'], filename)


@app.route('/download/<filename>')
def download_comp(filename):
    file_path = os.path.join(app.config['COMPRESSED_FOLDER'], filename)
    return send_file(file_path, as_attachment=True)


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
