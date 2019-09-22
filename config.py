import os

class Config:
    SECRET_KEY='0aea274cb6d66959e329887208e3365a'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://paul:leejones1@localhost/blog'


class ProdConfig(Config):
    pass


class DevConfig(Config):

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
