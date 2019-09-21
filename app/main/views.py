from . import main
from flask import render_template,redirect, url_for


@main.route('/')
def index():
    message="Hello everyone, welcome to whisper blogers"

    return render_template('index.html',message=message).