from flask import Flask, render_template, request, url_for, redirect, flash, request
from flask_sqlalchemy import SQLAlchemy
import randomizer
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '0c2d1a4bd71fc47b799b7b0de1daee0f'


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home():    
    if request.method == 'POST':
        zipCode = request.form['zip_code']
        return render_template('home.html', food=randomizer.food(), foodlist=randomizer.fastFoodDict, zipCode=zipCode)
    else:
        return render_template('home.html', food=randomizer.food(), foodlist=randomizer.fastFoodDict)

@app.route('/about')
def about():
    return render_template("about.html",title= "about")

@app.route('/mealchooser', methods=['POST', 'GET'])
def mealchooser():
    return render_template('mealchooser.html', food=randomizer.food(), foodlist=randomizer.fastFoodDict, title='mealchooser')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)

@app.route('/singup', methods=['GET','POST'])
def singup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("singup.html", title="sing-up", form=form)

@app.route('/promotions')
def promotions():
    return render_template("promotions.html",title= "promotions")

@app.route('/previous')
def previous():
    return render_template("previous.html",title= "previous")

if __name__ == "__main__":
    app.run(debug=True)
    

    