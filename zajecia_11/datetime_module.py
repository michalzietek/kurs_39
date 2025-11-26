from datetime import datetime, timedelta


print(datetime.today().date())

print(datetime.now().date() + timedelta(days=12))

data_amerykanska = "2025/24/11"


format = "%Y/%d/%m"

data_faktyczna = datetime.strptime(data_amerykanska, format)

print(data_faktyczna)


"""
format:
%m - miesiac
%d - dzien
%Y - pelny rok
%y - niepelny rok (23)
%H - godzina
%M - minuta
%S - sekunda
"""