import sqlite3
class DBManager:
    def __init__(self, db_path="save.db"):
        self.conn = sqlite3.connect(db_path)
    def save_player_state(self, player_data): pass
