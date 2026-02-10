import logging

from flask import Flask, render_template

from routes import my_blueprint

from models import Saldo

from database import db


def create_app():
    app = Flask(__name__)
    app.secret_key = "my_secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ksiegarnia_kurs39.db"
    db.init_app(app)

    # Logowanie: poziom INFO w konsoli
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    logger = logging.getLogger(__name__)

    app.register_blueprint(my_blueprint)


    with app.app_context():
        db.create_all()
        saldo = db.session.query(Saldo).first()
        if not saldo:
            default_saldo = Saldo(value=10000.0)
            db.session.add(default_saldo)
            db.session.commit()


    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
