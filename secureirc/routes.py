from secureirc import app, db
from secureirc.forms import LoginForm, RegistrationForm, RoomCreationForm
from secureirc.models import User, Room
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_login import current_user, login_user, logout_user, login_required

import sys
import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.route('/<roomname>/userlist')
@login_required
def userlist(roomname):
    user_list = Room.query.filter_by(roomname=roomname).first().users
    print(user_list, file=sys.stderr)
    return render_template('userlist.html', users=user_list)

@app.route('/roomlist')
@login_required
def roomlist():
    room_list = Room.query.filter_by(public=True)
    return render_template('roomlist.html', rooms=room_list)

@app.route('/createroom', methods=['GET', 'POST'])
@login_required
def create_room():
    form = RoomCreationForm()
    if form.validate_on_submit():
        rname = ""
        if form.roomname.data is "":
            rname = id_generator()
            #checks for collision
            if Room.query.filter_by(roomname=rname).first() is not None:
                rname = id_generator()
        else:
            rname = form.roomname.data

        room = Room(roomname=rname, public=form.pub_listed.data)
        if form.password.data is not "":
            room.set_password(form.password.data)

        room.users.append(current_user)
        db.session.add(room)
        db.session.commit()
        return redirect('/'+rname+'/chat')
    return render_template("createroom.html", form=form)

@app.route('/<roomname>/chat')
@login_required
def chat_room(roomname):
    room = Room.query.filter_by(roomname=roomname).first()
    if room is None:
        abort(404)
    if room.password_hash is not None:
        room.users.append(current_user)    
        db.session.commit()
    else:
        return render_template('passwordprompt.html', room=roomname)
    return render_template('chat.html', room=roomname)


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
        flash('Successfully created user.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if(current_user.is_authenticated):
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if (user is None) or (not user.check_password(form.password.data)):
            flash('Invalid username/password', 'danger')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)
        return redirect('index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

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

@app.route('/<room>/chat_script')
@login_required
def chat_script_room(room):
    return render_template('chat.js', roomname=room)


@app.route('/keys/<user>')
def get_key(user):
    key = User.query.filter_by(username=user).first().publickey
    return key
#   if (key is None):
#      return None 
#TODO: Handle the key being empty
#   else:
#      return key
#from secureirc.events import userlist #I'm being VERY naughty here
#return userlist[user];
