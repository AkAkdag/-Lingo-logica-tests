import random

class Lingo:
    def __init__(self):
        self.woord = self.generate_woord()
        self.poging = 0

    def generate_woord(self):
        woorden = ['appel', 'auto']
        return random.choice(woorden)

    def check_gok(self, gok):
        if len(gok) != len(self.woord):
            return False

        for i in range(len(self.woord)):
            if self.woord[i] == gok[i]:
                print('G', end='')
            elif gok[i] in self.woord:
                print('O', end='')
            else:
                print('R', end='')

        print()
        return gok == self.woord

    def play(self):
        print("Welkom bij Lingo!")
        print("Raad het woord van 5 letters.")
        print("De letters kunnen Groen (G), Oranje (O) of Rood (R) zijn.")
        print("Groen betekent dat de letter correct is.")
        print("Oranje betekent dat de letter voorkomt in het woord, maar niet op de juiste positie.")
        print("Rood betekent dat de letter niet voorkomt in het woord.")

        while True:
            gok = input("Doe een gok: ").lower()
            self.poging += 1

            if self.check_gok(gok):
                print("Gefeliciteerd! Je hebt het woord geraden in", self.poging, "pogingen.")
                break

            if self.poging == 5:
                print("Helaas, je hebt het woord niet kunnen raden.")
                print("Het woord was:", self.woord)
                break

game = Lingo()
game.play()
