from flask import Blueprint, render_template, request, Response, flash
from ksiegozbior import get_bookstore_state, change_saldo, rent_a_book, buy_book, show_history
from werkzeug.exceptions import HTTPException

my_blueprint = Blueprint("my_blueprint", __name__)

@my_blueprint.route("/", methods=["GET", "POST"])
def home_view():
    if request.method == "POST":
        form_type = request.form.get("form_type")
        if form_type == "change_saldo":
            new_saldo = request.form.get("new_saldo")
            change_saldo(new_saldo)
        elif form_type == "rent_a_book":
            numer_isbn = request.form.get("ISBN_rent")
            rent_a_book(numer_isbn)
        elif form_type == "buy_book":
            status_code = buy_book(
                tytul=request.form.get("tytul"),
                autor=request.form.get("autor"),
                isbn=request.form.get("ISBN"),
                rok_wydania=request.form.get("rok_wydania"),
                cena=float(request.form.get("cena")),
                kategoria=request.form.get("kategoria"),
                ilosc=int(request.form.get("ilosc", 1)),
            )
            if status_code == 500:
                # raise HTTPException("Niestety nie stać Cię na kupno tej książki")
                #return Response(status=status_code, response="Niestety nie stać Cię na kupno tej książki!")
                flash("Niestety nie stać Cię na kupno tej książki")
    state = get_bookstore_state()
    # return render_template("ksiegarnia.html", saldo=state.get("saldo"), books=state.get("books"), historia=state.get("historia")) to jest tożsame z tym na dole!!
    return render_template("ksiegarnia.html", **state)


@my_blueprint.route("/history/<od>/<do>")
@my_blueprint.route("/history")
def history_view(od=None,do=None):
    history = show_history(od, do)
    return render_template("history.html", history=history)