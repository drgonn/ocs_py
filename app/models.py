from app import db


class Stock(db.Model):
    __tablename__ = 'stock'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    ticker = db.Column(db.String(255))
    cik = db.Column(db.String(255))
    stype = db.Column(db.String(255))
    sic = db.Column(db.Integer, index=True)
    sector = db.Column(db.String(255))
    delisted = db.Column(db.Boolean, default=False)

