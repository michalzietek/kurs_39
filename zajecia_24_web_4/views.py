from flask.views import MethodView
from flask import Blueprint

users_blueprint = Blueprint("users_blueprint", __name__)

class UsersView(MethodView):
    def get(self):
        return "List of users"

    def post(self):
        return "Creating a user"

    def put(self):
        return "Updating a user"

    def delete(self):
        return "Deleting a user"

users_view = UsersView.as_view("users")

users_blueprint.add_url_rule("/users", view_func=users_view, methods=["GET", "POST", "PUT", "DELETE"])