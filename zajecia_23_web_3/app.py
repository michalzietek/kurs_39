from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {
        "name": "Michał",
        "surname": "Ziętkowski",
        "age": 22
    },
    {
        "name": "Anna",
        "surname": "Nowak",
        "age": 30
    },
    {
        "name": "Bogdan",
        "surname": "Kowalski",
        "age": 56
    }
]

@app.route("/hghghgh")
def main_view():
    return render_template("index.html", wiek=22)

@app.route("/dynamic/<name>")
@app.route("/dynamic/")
def dynamic_endpoint(name=None):
    return render_template("index.html", imie=name, wiek=12)

@app.route("/hello")
def hello_world():
    return "Hello user!"

@app.route("/users", methods=["GET", "POST"])
def show_users():
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        age = request.form.get("age")
        users.append({
            "name": name, "surname": surname, "age": age
        })
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)