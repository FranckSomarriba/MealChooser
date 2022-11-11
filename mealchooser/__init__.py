import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_login import LoginManager
from flask_login import UserMixin


app = Flask(__name__)
app.config['SECRET_KEY'] = '0c2d1a4bd71fc47b799b7b0de1daee0f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'          # Databse with relative path creation
db = SQLAlchemy(app)    # Creation of Database
bcrypt = Bcrypt(app)    # Creation of password hashing
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googleemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)
from mealchooser import routes