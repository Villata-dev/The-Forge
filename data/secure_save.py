import json
import base64

class SecureSaveSystem:
    SAVE_FILE = "data/secure_save.dat"

    @classmethod
    def save(cls, data: dict):
        json_str = json.dumps(data)
        encoded = base64.b64encode(json_str.encode('utf-8')).decode('utf-8')
        with open(cls.SAVE_FILE, 'w') as f:
            f.write(encoded)

    @classmethod
    def load(cls) -> dict:
        try:
            with open(cls.SAVE_FILE, 'r') as f:
                encoded = f.read()
            json_str = base64.b64decode(encoded.encode('utf-8')).decode('utf-8')
            return json.loads(json_str)
        except Exception:
            return {}
