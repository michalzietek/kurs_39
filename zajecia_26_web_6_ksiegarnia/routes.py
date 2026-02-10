import logging

from flask import Blueprint, render_template, request, flash

from ksiegozbior import (
    get_bookstore_state,
    change_saldo,
    rent_a_book,
    buy_book,
    show_history,
)

logger = logging.getLogger(__name__)

my_blueprint = Blueprint("my_blueprint", __name__)

# Komunikat dla użytkownika przy nieoczekiwanym błędzie (bez szczegółów technicznych)
_UNEXPECTED_ERROR_MSG = "Wystąpił nieoczekiwany błąd. Spróbuj ponownie lub skontaktuj się z administratorem."


@my_blueprint.route("/", methods=["GET", "POST"])
def home_view():
    if request.method == "POST":
        form_type = request.form.get("form_type")
        try:
            if form_type == "change_saldo":
                ok, msg = change_saldo(request.form.get("new_saldo"))
                flash(msg, "success" if ok else "danger")
            elif form_type == "rent_a_book":
                ok, msg = rent_a_book(request.form.get("ISBN_rent"))
                flash(msg, "success" if ok else "danger")
            elif form_type == "buy_book":
                ok, msg = buy_book(
                    tytul=request.form.get("tytul"),
                    autor=request.form.get("autor"),
                    isbn=request.form.get("ISBN"),
                    rok_wydania=request.form.get("rok_wydania"),
                    cena=request.form.get("cena"),
                    kategoria=request.form.get("kategoria"),
                    ilosc=request.form.get("ilosc", 1),
                )
                flash(msg, "success" if ok else "danger")
            elif form_type:
                flash("Nieznany typ operacji.", "danger")
        except Exception as e:
            logger.exception("Błąd w home_view (form_type=%s): %s", form_type, e)
            flash(_UNEXPECTED_ERROR_MSG, "danger")
    try:
        state = get_bookstore_state()
    except Exception as e:
        logger.exception("Błąd ładowania stanu księgarni: %s", e)
        flash(_UNEXPECTED_ERROR_MSG, "danger")
        state = {"saldo": 0, "ksiegozbior": [], "historia": []}
    return render_template("ksiegarnia.html", **state)


@my_blueprint.route("/history")
@my_blueprint.route("/history/<od>/<do>")
def history_view(od=None, do=None):
    try:
        history = show_history(od, do)
    except Exception as e:
        logger.exception("Błąd ładowania historii (od=%s, do=%s): %s", od, do, e)
        flash("Nie udało się załadować historii. Spróbuj ponownie.", "danger")
        history = []
    return render_template("history.html", history=history)
