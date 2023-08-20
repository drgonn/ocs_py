from app import db

class Stock(db.Model):
	__tablename__ = 'stocks'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	ticker = db.Column(db.String(64))