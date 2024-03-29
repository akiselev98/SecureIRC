from flask import Flask
from flask_socketio import SocketIO
from flask_session import Session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#from flask_sslify import SSLify
from secureirc.config import Config

app = Flask(__name__)

login = LoginManager(app)
login.login_view = 'login'

app.config.from_object(Config)
db = SQLAlchemy(app)
#sslify = SSLify(app)
migrate = Migrate(app,db)

app.config['SECRET_KEY'] = 'aGVsbG8gZGFya25lc3MgbXkgb2xkIGZyaWVuZAo='
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
app.debug = True
app.host = '0.0.0.0'

bootstrap = Bootstrap(app)
Session(app)
socketio = SocketIO(app, manage_session=False)
socketio.init_app(app)

if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'))
    
import secureirc.routes
import secureirc.events
import secureirc.models

