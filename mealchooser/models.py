from mealchooser import db, login_manager, app
from mealchooser import app
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask_login import UserMixin
from flask_login import LoginManager
from flask import current_app as app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(20), unique=True, nullable=False)
    food_type = db.Column(db.String(20), unique=True, nullable=False)
    url = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"Food('{self.food_name}', '{self.food_type}')"

# with app.app_context():
#     db.create_all()