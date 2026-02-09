import json
#
#
# def load_data():
#     with open("ksiegarnia_example.json") as file:
#         # text = file.read()
#         # list_text = text.split("}")
#         # print(list_text)
#         text = json.load(file)
#         print(text)
#
# load_data()

class FileHandler:
    def __init__(self, filepath):
        self.file = filepath
        # self.krotka = self.load_data_from_file()
        # self.saldo = self.krotka[0]
        # self.historia = self.krotka[1]
        # self.ksiegozbior = self.krotka[2]
        self.saldo, self.historia, self.ksiegozbior = self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.file, encoding="utf-8") as file:
            data = json.load(file)
            return data.get("saldo"), data.get("historia"), data.get("ksiegozbior")

    def save_data_to_file(self, new_saldo, new_historia, new_ksiegozbior):
        with open(self.file, mode="w", encoding="utf-8") as file:
            temporary_data = {
                "saldo": new_saldo,
                "historia": new_historia,
                "ksiegozbior": new_ksiegozbior
            }
            file.write(json.dumps(temporary_data, indent=4, ensure_ascii=False))


file_handler = FileHandler("ksiegarnia.json")
