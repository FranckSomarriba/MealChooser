from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '0c2d1a4bd71fc47b799b7b0de1daee0f'

from mealchooser import routes