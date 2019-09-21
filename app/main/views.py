from . import main
from flask import render_template,redirect, url_for


@main.route('/')
def index():
    message="Hello everyone, welcome to whisper blogers"

    return render_template('index.html',message=message)

@main.route('/about')
def about():
    about_message="We post anything that comes in mind"

    return render_template('about.html',about_message=about_message)