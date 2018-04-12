from secureirc import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    users = ["akiselev", "cannonhead2", "moot", "Robert\'; DROP TABLE Users;--"]
    return render_template('chat.html', users=users)
