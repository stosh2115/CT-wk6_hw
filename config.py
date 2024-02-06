import os 
from dotenv import load_dotenv


basedir= os.path.abspath(os.path.dirname(__file__))


class config():
    FLASK_app = os.environ.get('FLASK_APP')
    Flask_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')