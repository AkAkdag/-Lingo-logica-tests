import sqlite3
from highscores import Highscores



class Lingo:

    def __init__(self):
        self.woord = str.lower(self.set_woord())
        self.beurt = 1
        


    def set_woord(self):
        connection = sqlite3.connect('lingo.sqlite3')
        cursor = connection.execute('SELECT * FROM vijfletters ORDER BY RANDOM() LIMIT 1;')
        for row in cursor:
            woord = row [0]
        connection.close()
        print(woord)
        return woord




    def validate_input(self, invoer, naam):
        
        # Verhoog de beurt
        self.beurt += 1

        # Converteer de invoer naar kleine letters
        invoer = str.lower(invoer)   

        # Controleer of de invoer string gelijk is aan het te raden woord
        if invoer == self.woord:
            # Voeg de score toe aan de database
            score = Highscores()
            score.add_score(naam, self.beurt)

            # Retourneer de feedback
            return "Gewonnen"    
        
        # Controleer of het woord 5 letters heeft
        if len(invoer) != 5:
            return "Voer een woord in van 5 letters"
        
        # Vergelijk elke letter van de invoerstring met het te raden woord
        uitvoer = ""
        for i in range(5):
            if invoer[i] == self.woord[i]:
                uitvoer += str.upper(invoer[i])
            
            # 
            # self.woord = "Lingo"
            # self.woord[i] = "L" > i = 0
            # self.woord[i] = "i" > i = 1
            # 
            elif invoer[i] in self.woord:    
                uitvoer += invoer[i]
            else:
                uitvoer += "_"   

        
    

        return uitvoer          
        # Geef de string terug
        return "OK"
