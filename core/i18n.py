import json

class Localization:
    _strings = {}
    _current_lang = "en"

    @classmethod
    def load_language(cls, lang_code: str):
        try:
            with open(f"locales/{lang_code}.json", 'r', encoding='utf-8') as f:
                cls._strings = json.load(f)
                cls._current_lang = lang_code
        except FileNotFoundError:
            cls._strings = {}

    @classmethod
    def get(cls, key: str, default: str = "") -> str:
        return cls._strings.get(key, default or key)
