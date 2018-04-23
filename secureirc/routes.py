from secureirc import app, db
from secureirc.forms import LoginForm, RegistrationForm
from secureirc.models import User
from flask import Flask, render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user

import sys

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/userlist')
def userlist():
    from secureirc.events import userlist # TODO: replace with database voodoo
    print(userlist.keys(), file=sys.stderr)
    return render_template('userlist.html', users=userlist.keys())

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if(current_user.is_authenticated):
        return redirect(url_for('/'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if (user is None) or (not user.check_password(form.password.data)):
            flash('Invalid username/password')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/validation', methods = ['POST'])
def validation():
    name = request.form['name']
    password = request.form['password']


@app.route('/chat')
def chat():
    #print("Serving chat.", file=sys.stderr)
    #print("Serving chat.", file=sys.stdout)
    #users = ["akiselev", "cannonhead2", "moot", "Robert\'; DROP TABLE Users;--"]
    return render_template('chat.html')

@app.route('/keys/<user>')
def get_key(user):
    from secureirc.events import userlist #I'm being VERY naughty here
    return userlist[user];
    
#@app.route('/chat/<username>')
#def chat_user(username=username):
    
