from highscores import Highscores
import sqlite3

# Test het maken van de tabel

scores = Highscores()


connection = sqlite3.connect('lingo.sqlite3')
cursor = connection.cursor()
cursor.execute("DROP TABLE highscores; ")
connection.close()

