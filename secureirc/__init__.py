from flask import Flask
from flask_socketio import SocketIO
import routes
app = Flask(__name__)
app.config['SECRET_KEY'] = 'aGVsbG8gZGFya25lc3MgbXkgb2xkIGZyaWVuZAo='
socketio = SocketIO(app)
app.debug = True


@app.route('/')
def test():
	return 'Test successful'

if __name__ == "__main__":
    socketio.run(app, log_output=True)
    
#import secureirc.routes
#import routes
#import secureirc.events
