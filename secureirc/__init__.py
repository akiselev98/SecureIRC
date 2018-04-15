from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aGVsbG8gZGFya25lc3MgbXkgb2xkIGZyaWVuZAo='
socketio = SocketIO(app)
app.debug = True

if __name__ == "__main__":
    socketio.run(app, log_output=True)
    
import secureirc.routes
import secureirc.events
