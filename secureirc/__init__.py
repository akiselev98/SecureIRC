from flask import Flask
from flask_socketio import SocketIO
from flask_session import Session
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app import routes, models

app.config['SECRET_KEY'] = 'aGVsbG8gZGFya25lc3MgbXkgb2xkIGZyaWVuZAo='
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
socketio = SocketIO(app, manage_session=False)
app.debug = True
app.host = '0.0.0.0'


if __name__ == "__main__":
    socketio.run(app, log_output=True)
    
import secureirc.routes
import secureirc.events
