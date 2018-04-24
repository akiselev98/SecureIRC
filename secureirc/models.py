from secureirc import db, login
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    publickey = db.Column(db.String(256))
                              
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    


class Room(db.Model):
    __tablename__ = 'rooms'
    #do not allow duplicate room names
    roomName = db.Column(db.String(128), primary_key = True, index = True, unique = True)
    keyset = db.Column(db.String(256))
   
    def __repr__(self):
        return '<Room ()>'.format(self.roomName)
