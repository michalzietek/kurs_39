from flask import Blueprint

my_blueprint = Blueprint("my_blueprint", __name__)

@my_blueprint.route("/", methods=["GET", "POST"])
def main_view():
    return "Hello world"