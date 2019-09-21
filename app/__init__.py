from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options



bootstrap = Bootstrap()

def create_app():
    app=Flask(__name__)


    app.config.from_object(config_options['development'])
    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


    return app