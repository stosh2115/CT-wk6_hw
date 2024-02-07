from werkzeug.security import generate_password_hash 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager, UserMixin 
from datetime import datetime 
import uuid 


# instantiate all of our classes
db = SQLAlchemy() 
login_manager = LoginManager()


#use login_manger ogject to create our user_loader function
@login_manager.user_loader
def load_user(user_id):
    """Given *user_id*, return the associated User object
    
    :parametet unicode user_id: user_id is user to retrieve
    """

    return User.query.get(user_id) 



class User(db.Model, UserMixin):
    user_id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    #INSERT INTO, USER() Values()
    def __init__(self, username, email, password, first_name="",last_name=""):
        self.user_id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = self.set_password(password)


    #methods for editing our attributes
    def set_id(self):
        return str(uuid.uuid4()) 
    
    def get_id(self):
        return str(self.user_id) 
    
    def set_password(self, password):
        return generate_password_hash(password) 
    
    def __repr__(self):
        return f"<User: {self.username}>"