# Hier importeer je tkinter afgekort als tk

import tkinter as tk


# Hier maak je een klasse (Raad)
# Met behulp van Innit methode maakt GUI elementen Tkinter widgets
#  Door het main-venster aan de Raad-instantie (classe) door te geven, kunnen we de GUI-elementen en functionaliteit binnen dat venster maken en beheren.
# Het woord 'main' is in dit geval een willekeurige naam die wordt gebruikt om te verwijzen naar het hoofdvenster
class Raad: 
    def __init__(self, main): 
        self.woord = "aarde"
        self.main = main
        self.main.title("Woord raden")  

        self.speel_label = tk.Label(main, text="Raad een woord:")
        self.speel_label.pack()

        self.speel_entry = tk.Entry(main)
        self.speel_entry.pack()

        self.speel_button = tk.Button(main, text="Raad", command= self.spelen)
        self.speel_button.pack()


#  Door  validate_input functie letters van een meegegeven woord wordt vergeleken met het te raden woord.
    def validate_input(self, input_woord):
        if len (input_woord) != 5:
         return False
        
        elif input_woord == self.woord:
            return True
        
        else:
            return False    
        

# Hier maken we een functie die spelen heet en geven we self als een parameter self verwijst naar het object (de instantie van de klasse (Raad)) waaraan de methode wordt opgeroepen. 
# Als je wil je kan ook een andere naam geven in plaats van "self"
    def spelen(self):
        geraden = self.speel_entry.get()
        uitslag = self.validate_input(geraden)
        if uitslag:
            self.uitkomst_label.config(text="Je hebt het woord geraden :)")
        else:
            self.uitkomst_label.config(text="Jammer. Je hebt het woord niet geraden!")

# Hier maken we een functie die uitvoer heet en geven we self als een parameter self verwijst naar het object (de instantie van de klasse (Raad)) waaraan de methode wordt opgeroepen. 
# Hier verbinden we attribuut (uitkomt) van vorige functie met behulp van self parameter 
    def uitvoer(self):
        self.uitkomst_label = tk.Label(self.main, text="")
        self.uitkomst_label.pack()
        self.main.mainloop()              


# Hier noemen we de klasse en functies zodat het programma wordt gestart
window = tk.Tk()
woord = Raad(window)
woord.uitvoer()

