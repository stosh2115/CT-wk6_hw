from flask import Flask
from flask_migrate import Migrate

from config import config
from .models import login_manager, db
from .blueprints.site.routes import site
from .blueprints.auth.routes import auth


app = Flask(__name__)

app.config.from_object(config)


login_manager.init_app(app)
login_manager.login_view = 'auth.sign_id' #authentication route
login_manager.login_message = 'Hey you! Login Please'
login_manager.login_message_category = 'warning'


app.register_blueprint(site)
app.register_blueprint(auth)



db.init_app(app)
migrate = Migrate(app,db)


