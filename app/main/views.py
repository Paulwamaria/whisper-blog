from . import main
import requests
from ..models import User,Post,Quote
from flask_login import login_required
from flask import render_template, redirect, url_for,request


@main.route('/')
def index():
    message = "Welcome to Whisper Blogers"
    page = request.args.get('page', 1, type=int)
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=2) 
    quote_data = requests.get('http://quotes.stormconsultancy.co.uk/random.json' ).json()
    quote_content= quote_data.get('quote')
    quote_author= quote_data.get('author')
    
    return render_template('index.html', message=message, posts=posts,quote=quote_content,author=quote_author)


@main.route('/about')
def about(): 
    quote_data = requests.get('http://quotes.stormconsultancy.co.uk/random.json' ).json()
    quote_content= quote_data.get('quote')
    quote_author= quote_data.get('author')
    

    about_message = "We post anything that promotes mental health"

    return render_template('about.html', about_message=about_message,quote=quote_content,author=quote_author)

@main.route('/user/<string:username>')
def user_posts(username):
    quote_data = requests.get('http://quotes.stormconsultancy.co.uk/random.json' ).json()
    quote_content= quote_data.get('quote')
    quote_author= quote_data.get('author')
    
 
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts=Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
            .paginate(page=page,per_page=2) 

    return render_template('user_post.html', posts=posts, user=user,quote=quote_content,author=quote_author)

