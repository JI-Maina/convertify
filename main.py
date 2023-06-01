#!/usr/bin/python3

from flask import Flask, render_template, url_for, flash, redirect, send_from_directory
from forms import RegistrationForm, LoginForm, UploadForm
from flask_uploads import UploadSet, IMAGES, configure_uploads

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd9eed75c59d795794daa7129'
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)


@app.route("/uploads/<filename>")
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)


@app.route("/", methods=['GET', 'POST'])
def home():
    """represents site homepage"""
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file', filename=filename)
    else:
        file_url = None
    return render_template('home.html', form=form, file_url=file_url)


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


if __name__ == '__main__':
    app.run(debug=True)
