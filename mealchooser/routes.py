import os
import secrets
from flask import render_template, request, url_for, redirect, flash, abort
from mealchooser import app, db, bcrypt, mail
from mealchooser import site_functions
from mealchooser.models import User
from mealchooser.forms import RegistrationForm, LoginForm
from mealchooser.forms import RequestResetForm,ResetPasswordForm
from flask_mail import Message
from flask_login import current_user, login_user, logout_user, login_required


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

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template("signup.html", title="sing-up", form=form)

@app.route('/promotions')
def promotions():
    return render_template("promotions.html",title= "promotions")

@app.route('/previous')
def previous():
    return render_template("previous.html",title= "previous")

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To reset your password visit the following link:
{url_for('reset_token', token =token,_external = True)}

If you did not made this request simply ignore this email and no changes will be made
'''
    mail.send(msg)

@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
     if current_user.is_authenticated:
        return redirect(url_for('home'))
     form = RequestResetForm()
     if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email as been sent with instructions to reset your password.', 'info')
        return redirect(url_for('login'))
     return render_template('reset_request.html', title='Reset Password', form=form)
    
@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f'your password has been update! {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form = form)

def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/like/<int:post_id>/<action>')
def like_action(post_id, action):
    post = Post.query.filter_by(id=post_id).first_or_404()
    if action == 'like':
        session['user_id'].like_post(post)
        db.session.commit()
    if action == 'unlike':
        session['user_id'].unlike_post(post)
        db.session.commit()
    return redirect(request.referrer)