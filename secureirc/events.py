from secureirc import app, socketio

from flask_socketio import send, emit
from flask import session

import json
import sys

#print('Loaded events', file=sys.stderr)
userlist = {}
def handle_message(message):
    print('Got message from ' + session['username'], file=sys.stderr)
    emit('message', {'msg': message['msg']}, broadcast=True)

def handle_joined(data):
    session['username'] = data['username']
    print("User joined: "
          + session['username']
          + "(ID:"+data['id']+")",
          file=sys.stderr)
    userlist[session['username']] = data['key']
    emit('status', {'msg': "User joined: " + session['username'] + " (ID:"+data['id']+")"}, broadcast=True)
    #emit('status', {'msg': str(userlist)}, broadcast=True)
    emit('userlist_update', userlist, broadcast=True)
    #TODO: Add user and publickey to database.

def handle_disconnect():
    print("User Disconnected: " + session['username'], file=sys.stderr)
    userlist[session['username']] = None
    emit('userlist_update', userlist, broadcast=True)
    emit('status', {'msg': session['username']+" disconnected."}, broadcast=True)
    
socketio.on_event('text', handle_message, namespace='/chat')
socketio.on_event('joined', handle_joined, namespace='/chat')
socketio.on_event('disconnect', handle_disconnect, namespace='/chat')
