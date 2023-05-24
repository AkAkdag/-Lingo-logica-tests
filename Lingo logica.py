
class Raad:
    def __init__(self): 
        self.woord = "aarde"

    def validate_input(self, input_woord):
        if len (input_woord) != 5:
         return False
        
        elif input_woord == self.woord:
            return True
        
        else:
            return False    


woord = Raad()

geraden = input ("Doe een gok ")
uitslag = woord.validate_input(geraden)
if uitslag:
    print("Je hebt het woord geraden :)")
else:
    print("Jammer. Je hebt het woord niet geraden!")


