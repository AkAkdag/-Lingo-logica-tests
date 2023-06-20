from tkinter import *
from lingo import Lingo
from mytimer import Timer

# Lingo object
lingo = Lingo()
timer = Timer()


# Lijst van input velden
invoervelden = {}


# Validate input, event listener
def validate(event):
    print("beurt: " + str(lingo.beurt))
    print("woord: " + lingo.woord)

    invoer = invoervelden[lingo.beurt - 1].get()
    print("ingevoerd: " + invoer)

    uitvoer = lingo.validate_input(invoer, naam_veld.get())
    print("resultaat: " + uitvoer)

    # Geef de uitvoer weer
    invoervelden[lingo.beurt - 2].insert(END, " > " + uitvoer)

    # Status bijwerken
    status_label.config(text=uitvoer)

    # Beurten bijwerken
    beurten_label.config(text=str(lingo.beurt) + "/5")

    # Timer starten, resetten en stop zetten.
    if lingo.beurt == 1:
        timer.reset() 
        timer.start()  

    elif lingo.beurt == 6:
        timer.reset()

    elif invoer == lingo.woord:
        timer.stop()

# Main
app = Tk()
app.title("Lingo!")
app.geometry("300x400")
app.resizable(False, False)


# Tittel
titel_label = Label(app, text="Welkom bij Lingo!", font=("Arial", 18, "bold"))
titel_label.pack()

# Uitleg
inro_label = Label(app, text="Raad het woord van vijf letters in vijf beurten")
inro_label.pack()

# Naam van Speler
naam_veld = Entry(app)
naam_veld.pack()

# Timer label
timer_label = Label(app, text="Tijd: 0 seconden", font=("Arial", 12))
timer_label.pack()


# Status
status_label = Label(app, text="Succes", font=("Arial", 14, "bold"), fg='red')
status_label.pack()

# Beurten tellen
beurten_label = Label(app, text="1/5", font=("Arial", 14, "bold"))
beurten_label.pack()

# Input velden
for r in range(5):
    invoerveld = Entry(app, bg='blue', justify=LEFT, font=("Arial", 24, "bold"), fg='white')
    invoerveld.pack()
    invoervelden[r] = invoerveld
    invoerveld.bind('<Return>', validate)




# Timer bijwerken
def update_timer():
    verstreken_time = timer.get_verstreken_time()
    timer_label.config(text="Tijd: {:.0f} seconden".format(verstreken_time))

    app.after(100, update_timer)


# Timer starten
timer.start()

update_timer()

app.mainloop()
