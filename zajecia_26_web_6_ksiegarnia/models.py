from database import db

class Saldo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ISBN = db.Column(db.String, unique=True)
    tytul = db.Column(db.String(100))
    autor = db.Column(db.String(100))
    rok = db.Column(db.Integer)
    cena = db.Column(db.Float)
    kategoria = db.Column(db.String(100))
    ilosc_na_stanie = db.Column(db.Integer)
    ilosc = db.Column(db.Integer)

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(200))