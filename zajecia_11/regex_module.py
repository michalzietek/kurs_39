import re

regular_expression = r"[a-zA-Z0-9._]+\@[a-zA-Z0-9._]+\.[a-zA-Z0-9._]{2,}"

wiersz_o_emailach = """
W cyfrowym świecie, gdzie dane fruwają,
Maile codziennie skrzynki zalewają.
Pisze Ada z rana – ada.nowak@poczta.pl,
A potem wiadomość – od Marka sygnał.

marek123@onet.eu – w tytule "Pilne",
Choć treść jak zwykle: "Spotkajmy się w Wilnie".
zosia.kwiat@firma.com przysyła fakturę,
A admin@bezpiecznie.net – alert o strukturze.

Na koniec robot7@gmail.com pisze: "Hello!",
Choć nikt nie wie, czy to człowiek, czy AI zgoła...
"""

emails = re.findall(regular_expression, wiersz_o_emailach)
for email in emails:
    valid_email = re.match(regular_expression, email)
    print(valid_email)
print(emails)