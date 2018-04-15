from secureirc import app, socketio

from flask_socketio import send, emit
import sys

print('Loaded events', file=sys.stderr) 

def handle_message(message):
    print('Got message!', file=sys.stderr)
    emit('message', {'msg': message['msg']}, broadcast=True)
    
socketio.on_event('text', handle_message, namespace='/chat')
