from lingo import Lingo
# Maak een instantie van lingo
mijnLingo = Lingo()


# Test het woord uit de database
uitvoer = mijnLingo.woord   
if (len(uitvoer) == 5):
    print("TEST OK! - Er is een woord van 5 letters geselecteerd: " + uitvoer)
else:
    print("FAIL: Er is geen woord geselecteerd" + uitvoer)
print('')        

# Controleer het woord
print(mijnLingo.validate_input("lingo"))


# Test de juiste lengte

uitvoer = mijnLingo.validate_input("lin")
if (uitvoer == "Voer een woord in van 5 letters"):
    print("Test OK! - de juiste lengte: " + uitvoer )
else:    
    print("Test FAILED! - de juiste lengte: " + uitvoer )


uitvoer = mijnLingo.validate_input("lin")
if (uitvoer == "Voer een woord in van 5 letters"):
    print("Test OK! - de juiste lengte: " + uitvoer )
else:    
    print("Test FAILED! - de juiste lengte: " + uitvoer )    

invoer = "liaaa"
uitvoer = mijnLingo.validate_input(invoer)
if (uitvoer == "LI___"):
    print("Test OK! - de juiste letters op juiste plek: " + invoer + " > " + uitvoer )
else:    
    print("Test FAILED! - de juiste letters op juiste plek: " + invoer + " > " + uitvoer)  
    
invoer = "aaali"
uitvoer = mijnLingo.validate_input(invoer)
if (uitvoer == "___li"):
    print("Test OK! - de juiste letters op juiste plek: " + invoer + " > " + uitvoer )
else:    
    print("Test FAILED! - de juiste letters op juiste plek: " + invoer + " > " + uitvoer) 


invoer = "aaaaa"
uitvoer = mijnLingo.validate_input(invoer)
if (uitvoer == "_____"):
    print("Test OK! - de juiste letters op juiste plek: " + invoer + " > " + uitvoer )
else:    
    print("Test FAILED! - de juiste letters op juiste plek: " + invoer + " > " + uitvoer)                       
