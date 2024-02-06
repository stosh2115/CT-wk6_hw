from flask import Flask
from config import config
from .blueprints.site.routes import site


app = Flask(__name__)

app.config.from_object(config)


app.register_blueprint(site)


