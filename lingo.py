
class Lingo:

    def __init__(self):
        self.woord = str.lower("Lingo")

    def validate_input(self, invoer):
        # Converteer de invoer naar kleine letters
        invoer = str.lower(invoer)   

        # Controleer of de invoerstring gelijk is aan het te raden woord
        if invoer == self.woord:
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
