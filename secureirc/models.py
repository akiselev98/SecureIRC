from secureirc import db, login
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    publickey = db.Column(db.String(256))
    room = db.Column(db.Integer, db.ForeignKey('room.id'))
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    
class Room(db.Model):
    __tablename__ = 'room'
    id = db.Column(db.Integer, primary_key=True, unique=True, index = True)
    #do not allow duplicate room names
    roomname = db.Column(db.String(32), index = True)
    users = db.relationship('User', backref='Room', lazy=True)
    password_hash = db.Column(db.String(128))
    public = db.Column(db.Boolean)
    
    def __repr__(self):
        return '<Room ()>'.format(self.roomName)
