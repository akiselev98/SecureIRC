from secureirc import db

class User(db.Model):
    __tablename__ = 'credentials'
    userName = db.Column(db.String(100), primary_key = True, index=True, unique=True)
    passWord = db.Column(db.String(128))
    #TODO: Hash passwords
    def __repr__(self):
        return '<User {}>'.format(self.userName)

#TODO: Add rooms
#something like room(db.Model) containing user objects

class Room(db.Model):
    #do not allow duplicate room names
    roomName = db.Column(db.String(128), primary_key = True, index = True, unique = True)
    
    
    def __repr__(self):
	#TODO
        doNoting = 2 + 2
        
