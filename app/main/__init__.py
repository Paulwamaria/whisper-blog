from flask import Blueprint



main = Blueprint('__main__',name)


from . import views, errors