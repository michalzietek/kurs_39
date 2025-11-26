import os
print(os.getcwd())
print(os.listdir())

os.chdir("/home/michal/future_collars")
print(os.getcwd())

# moje_haslo = "12345465565"

moje_haslo = os.environ.get("MOJE_HASLO")
print(moje_haslo)

my_path = "/home/agnieszka"

print(os.path.exists(my_path))