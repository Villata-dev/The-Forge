import json
class Localization:
    def __init__(self, lang="en"):
        with open(f"data/lang_{lang}.json", "r") as f: self.texts = json.load(f)
    def get(self, key): return self.texts.get(key, key)
