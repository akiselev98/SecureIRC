from secureirc import app, db
from secureirc.forms import LoginForm, RegistrationForm
from secureirc.models import User
from flask import Flask, render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

import sys

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/userlist')
@login_required
def userlist():
    #from secureirc.events import userlist # TODO: replace with database voodoo
    #This doesn't work. The userlist path needs to return the userlist
    #template containing all the users in the room.
    list = User.query.order_by(User.username.desc()).all()

    print(list.first(), file=sys.stderr)
    return render_template('userlist.html', users=list.first())

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
            #flash('Invalid username/password')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)
        return redirect('index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/validation', methods = ['POST'])
def validation():
    name = request.form['name']
    password = request.form['password']

@app.route('/chat')
@login_required
def chat():
    return render_template('chat.html')

@app.route('/chat_script')
@login_required
def chat_script():
    return render_template('chat.js')

@app.route('/keys/<user>')
def get_key(user):
    key = User.query.filter_by(username=user).first().publickey

 #   if (key is None):
#	return None 
    #TODO: Handle the key being empty
 #   else:
  #  	return key
    #from secureirc.events import userlist #I'm being VERY naughty here
    #return userlist[user];
