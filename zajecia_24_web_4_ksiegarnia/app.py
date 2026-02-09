from flask import Flask
from routes import my_blueprint

app = Flask(__name__)
app.secret_key = "my_secret_key"

app.register_blueprint(my_blueprint)


with app.app_context():
    ## pobrac dane z API i zaladowac do bazy danych
    print("Zobacz gdzie jesteś")

if __name__ == "__main__":
    app.run(debug=True)