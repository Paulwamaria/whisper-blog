from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import UserMixin
from . import login_manager
import requests


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True) 
    username = db.Column(db.String(255),unique=True, nullable=False)
    email = db.Column(db.String(255),unique=True, nullable=False)
    image_file = db.Column(db.String(255), nullable=False, default='default.jpg')
    pass_secure = db.Column(db.String(255), nullable=False)
    posts = db.relationship('Post',backref='author',lazy=True)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)




    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    


    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"




class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime, nullable = False, default =datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'), nullable = False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"


class Quote(db.Model):
    __tablename__ = 'quotes'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(255),nullable=False)
    quote = db.Column(db.String(255), nullable=False)
    quote_id = db.Column(db.Integer, nullable=False)
   
    def __repr__(self):
        return f"Quote('{self.quote}','{self.author}')"