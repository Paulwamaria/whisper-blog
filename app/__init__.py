from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
db=SQLAlchemy()
bcrypt=Bcrypt()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint,)

    return app
   