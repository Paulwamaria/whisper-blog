from . import main
from ..models import User,Post
from flask_login import login_required
from flask import render_template, redirect, url_for


@main.route('/')
def index():
    message = "Welcome to Whisper Blogers"

    posts=Post.query.all()

    return render_template('index.html', message=message, posts=posts)


@main.route('/about')
def about(): 


    about_message = "We post anything that promotes mental health"

    return render_template('about.html', about_message=about_message)
