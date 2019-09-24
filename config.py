import os

class Config:
    SECRET_KEY=('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://paul:leejones1@localhost/blog'


class ProdConfig(Config):
    pass


class DevConfig(Config):

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
