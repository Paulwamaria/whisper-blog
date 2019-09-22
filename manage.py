from app import create_app

from flask_script import Manager,Server
from config import config_options



app=create_app()

manager=Manager(app)
manager.add_command('server',Server)



if __name__=='__main__':
    manager.run()