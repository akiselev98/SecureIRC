from app import db

class User(db.Model):
	userName = db.Column(db.String(100), index = True, unique = True)
	passWord = db.Column(db.String(128));


	def __repr__(self):
	return '<User {}>'.format(self.userName)
