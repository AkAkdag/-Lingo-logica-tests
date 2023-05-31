from tkinter import *
from lingo import Lingo


# Lingo object
lingo = Lingo()


invoervelden = {}  
# Valideer de invoer, event listener
def validate(event):
    print("beurt: " + str(lingo.beurt))
    print("woord: " + lingo.woord)
    
    invoer = invoervelden[lingo.beurt-1].get() 
    print("ingevoerd: " + invoer)

    uitvoer = lingo.validate_input(invoer)
    print("resultaat: " + uitvoer)

    # Toon de uitvoer
    invoervelden[lingo.beurt-2].insert(END, " > " + uitvoer)

    # Update de status
    status_label.config(text = uitvoer)

    #Update beurten 
    beurten_label.config(text = str(lingo.beurt) + "/5")

# Main
app = Tk()
app.title("Lingo!")
app.geometry("300x400")
app.resizable(False, False)

# Titel
titel_label = Label(app, text = "Welkom bij Lingo!", font=("Arial", 18, "bold"))
titel_label.pack()

# Uitleg
inro_label = Label(app, text = "Raad het woord van vijf letters in vijf beurten")
inro_label.pack()

# Status
status_label = Label(app, text = "Succes", font=("Arial", 14, "bold"), fg = 'red')
status_label.pack()

# Aantal beurten
beurten_label = Label(app, text = "1/5", font=("Arial", 14, "bold"))
beurten_label.pack()

# Invoervelden
for r in range(5):
    invoerveld = Entry(app, bg= 'blue', justify= LEFT, font=("Arial", 24, "bold"), fg='white')
    invoerveld.pack()
    invoervelden[r] = invoerveld
    invoerveld.bind('<Return>', validate)
  

# Run
app.mainloop()