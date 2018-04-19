from secureirc import app
from secureirc.forms import LoginForm
from flask import render_template

import sys

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/userlist')
def userlist():
    from secureirc.events import userlist # TODO: replace with database voodoo
    print(userlist.keys(), file=sys.stderr)
    return render_template('userlist.html', users=userlist.keys())

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

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
    
