# Hier importeer je tkinter afgekort als tk

import tkinter as tk



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



    def validate_input(self, input_woord):
        if len (input_woord) != 5:
         return False
        
        elif input_woord == self.woord:
            return True
        
        else:
            return False    
        


    def spelen(self):
        geraden = self.speel_entry.get()
        uitslag = self.validate_input(geraden)
        if uitslag:
            self.uitkomst_label.config(text="Je hebt het woord geraden :)")
        else:
            self.uitkomst_label.config(text="Jammer. Je hebt het woord niet geraden!")




woord = Raad()

geraden = input ("Doe een gok ")
uitslag = woord.validate_input(geraden)
if uitslag:
    print("Je hebt het woord geraden :)")
else:
    print("Jammer. Je hebt het woord niet geraden!")

