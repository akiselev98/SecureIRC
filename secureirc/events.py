from secureirc import app, socketio

from flask_socketio import send, emit
from flask_login import current_user
from flask import session
from secureirc import db
from secureirc.models import User, Room
import json
import sys

#print('Loaded events', file=sys.stderr)
userlist = {}


def handle_message(message):
    print('Got message from ' + current_user.username, file=sys.stderr)
    emit('message', {'msg': message['msg']}, broadcast=True)

def handle_joined(data):
    #session['username'] = data['username']
    print("User joined: "
          + current_user.username
          + "(ID:"+data['id']+")",
          file=sys.stderr)
    userlist[current_user.username] = data['key']
    current_user.publickey = data['key']
    emit('status', {'msg': "User joined: " + current_user.username + " (ID:"+data['id']+")"}, broadcast=True)
    #emit('status', {'msg': str(userlist)}, broadcast=True)
    emit('userlist_update', userlist, broadcast=True)
    u = User(id = data['id'], username = current_user.username, password_hash = 'test', publickey = data['key'])
    db.session.add(u)
    db.session.commit()
    #TODO: Add user and publickey to database.

def handle_disconnect():
    print("User Disconnected: " + session['username'], file=sys.stderr)
    current_user.publickey = ""
    del userlist[current_user.username]
    emit('userlist_update', userlist, broadcast=True)
    emit('status', {'msg': current_user.username+" disconnected."}, broadcast=True)
    
socketio.on_event('text', handle_message, namespace='/chat')
socketio.on_event('joined', handle_joined, namespace='/chat')
socketio.on_event('disconnect', handle_disconnect, namespace='/chat')
