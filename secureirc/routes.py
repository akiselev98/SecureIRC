from secureirc import app
from flask import render_template
import sys

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    print("Serving chat.", file=sys.stderr)
    users = ["akiselev", "cannonhead2", "moot", "Robert\'; DROP TABLE Users;--"]
    return render_template('chat.html', users=users)

#@app.route('/chat/<username>')
#def chat_user(username=username):
    
