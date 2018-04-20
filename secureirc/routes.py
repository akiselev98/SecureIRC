from secureirc import app
from flask import Flask, render_template, request
import sys

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validation', methods = ['POST'])
def validation():
    name = request.form['name']
    password = request.form['password']

@app.route('/chat')
def chat():
    #print("Serving chat.", file=sys.stderr)
    #print("Serving chat.", file=sys.stdout)
    users = ["akiselev", "cannonhead2", "moot", "Robert\'; DROP TABLE Users;--"]
    return render_template('chat.html', users=users)

#@app.route('/chat/<username>')
#def chat_user(username=username):
    
