from . import main
from flask import render_template, redirect, url_for
posts = [
    {
        'author': 'Paul Wamaria',
        'title': 'Blog Post1',
        'content': 'First Post Content',
        'date_posted': 'September 20, 2019'
    },
    {
        'author': 'Wincott Wamaria',
        'title': 'Blog Post2',
        'content': 'Second Post Content',
        'date_posted': 'September 21, 2019'
    }

]

@main.route('/')
def index():
    message = "Welcome to Whisper Blogers"



    return render_template('index.html', message=message, posts=posts)


@main.route('/about')
def about(): 


    about_message = "We post anything that promotes mental health"

    return render_template('about.html', about_message=about_message)
