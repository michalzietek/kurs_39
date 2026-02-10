from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///zajecia_26.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(80))
    name = db.Column(db.String(40))
    surname = db.Column(db.String(100))
    address = db.Column(db.String, nullable=False, server_default="not provided")

with app.app_context():
    db.create_all()
    ### OPERACJA TWORZENIA REKORDOW W TABELI BAZY DANYCH
    # user = User(
    #     username="Tomek",
    #     password="123456",
    #     email="rafal@gmail.com",
    #     name="Tomek",
    #     surname="Magik"
    # )
    # db.session.add(user)
    # db.session.commit()

    #### DLA WAS - jak zaladowac dane na poczatku tylko raz
    # users = User.query.all()
    # if not users:
    #     pass
    #     #tworzymy uzytkownia

    #### OPERACJE WYSZUKIWANIA
    # users = User.query.all()
    # user_first = User.query.first()
    # print(users)
    # print(user_first)
    # rafal = User.query.filter_by(username="Rafal", email="rafal@gmail.com").first()
    # filtered_users = User.query.filter_by(password="12345").all()
    # print(rafal)
    # print(filtered_users)

    #### OPERACJE ZMIANY

    # michal = User.query.filter_by(username="Michal").first()
    # michal.email = "nowy_email@interia.pl"
    # db.session.add(michal)
    # db.session.commit()

    #### OPERACJE USUWANIA

    # rafal_to_remove = User.query.filter_by(username="Rafal").delete()
    # db.session.commit()

    # users = User.query.all()
    # for user in users:
    #     db.session.delete(user)
    # db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)