from flask import render_template, request, url_for, redirect, flash, request
from mealchooser import app, db, bcrypt
from mealchooser import site_functions
from mealchooser.forms import RegistrationForm
from mealchooser.models import User

@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home():    
    if request.method == 'POST':
        zipCode = request.form['zip_code']
        return render_template('home.html', food=site_functions.food(), foodlist=site_functions.fastFoodDict, zipCode=zipCode)
    else:
        return render_template('home.html', food=site_functions.food(), foodlist=site_functions.fastFoodDict)

@app.route('/about')
def about():
    return render_template("about.html",title= "about")

@app.route('/mealchooser', methods=['POST', 'GET'])
def mealchooser():
    return render_template('mealchooser.html', food=site_functions.food(), foodlist=site_functions.fastFoodDict, title='mealchooser')

@app.route('/singup', methods=['GET','POST'])
def singup():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username, email=form.email, password=form.password)
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("singup.html", title="sing-up", form=form)

@app.route('/promotions')
def promotions():
    return render_template("promotions.html",title= "promotions")

@app.route('/previous')
def previous():
    return render_template("previous.html",title= "previous")