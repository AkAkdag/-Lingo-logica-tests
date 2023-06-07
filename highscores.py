import sqlite3

class Highscores:

    def __init__(self):
        # Controleren of de tabel bestaat en eventueel aanmaken
        self.create_tabel()

    def create_tabel(self):
        connection = sqlite3.connect('lingo.sqlite3')
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS highscores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL
            );""")
        connection.close()