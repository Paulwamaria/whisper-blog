from app import create_app,db
from app.models import User,Post
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager,Server
from config import config_options



app=create_app()
migrate = Migrate(app,db)

manager=Manager(app)
manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User,Post =Post)



if __name__=='__main__':
    manager.run()