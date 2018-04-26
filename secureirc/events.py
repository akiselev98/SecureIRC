from secureirc import app, socketio

from flask_socketio import send, emit, join_room, leave_room
from flask_login import current_user
from flask import session
from secureirc import db
from secureirc.models import User, Room
import json
import sys

#print('Loaded events', file=sys.stderr)
#userlist = {}


def handle_message(message):
    print('Got message from ' + current_user.username + ":" + message['msg'], file=sys.stderr)
    emit('message', {'msg': message['msg']}, room=current_user.room.roomname)

def handle_joined(data):
    #session['username'] = data['username']
    print("User joined: "
          + current_user.username
          + "(ID:"+data['id']+")",
          file=sys.stderr)
    #userlist[current_user.username] = data['key']
    join_room(current_user.room.roomname)
    current_user.publickey = data['key']
    db.session.commit()
    emit('status', {'msg': "User joined: " + current_user.username + " (ID:"+data['id']+")"},
         room=current_user.room.roomname)
    #emit('status', {'msg': str(userlist)}, broadcast=True)
    userlist = {user.username : user.publickey for user in current_user.room.users}
    emit('userlist_update', userlist, room=current_user.room.roomname)

def handle_disconnect():
    print("User Disconnected: " + current_user.username, file=sys.stderr)
    room = current_user.room
    current_user.room.users.remove(current_user)
    current_user.publickey = ""
    db.session.commit()
    userlist = {user.username : user.publickey for user in room.users}
    emit('userlist_update', userlist,
         room=room.roomname)
    emit('status', {'msg': current_user.username+" disconnected."},
         room=room.roomname)
    leave_room(room.roomname)
    if len(room.users) == 0:
        print("Deleting room", file=sys.stderr)
        db.session.delete(room)
        db.session.commit()
    
socketio.on_event('text', handle_message, namespace='/chat')
socketio.on_event('joined', handle_joined, namespace='/chat')
socketio.on_event('disconnect', handle_disconnect, namespace='/chat')
