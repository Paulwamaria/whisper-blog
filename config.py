class Config:
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):

    DEBUGG=True

config_options={
    'production':ProdConfig
    'development':DevConfig
}