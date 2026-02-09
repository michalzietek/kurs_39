import json


class FileHandler:
    def __init__(self, filepath):
        self.file = filepath
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
