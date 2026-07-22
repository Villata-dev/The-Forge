import base64, json
class SaveManager:
    def save_game(self, data, filename="save.dat"):
        encoded = base64.b64encode(json.dumps(data).encode()).decode()
        with open(filename, "w") as f: f.write(encoded)
