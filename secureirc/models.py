from secureirc import db

class User(db.Model):
   
    userName = db.Column(db.String(100), primary_key = True, index=True, unique=True)
    passWord = db.Column(db.String(128))
    
    def __repr__(self):
        return '<User {}>'.format(self.userName)

#TODO: Add rooms
#something like room(db.Model) containing user objects
